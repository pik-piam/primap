"""Read the PRIMAPDB into native python datastructures

Copyright (C) 2020 Potsdam Institute for Climate Impact Research (PIK)

Incorporates code from the mat73 python package, which is
Copyright (C) 2019 Simon Kern

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import datetime

import h5py
import numpy as np
import scipy as sp
import scipy.io
import tqdm
import typing
import xarray as xr
import pandas as pd


class MatFileHandle:
    def __init__(self, group: typing.Union[h5py.Group, np.ndarray, h5py.Dataset], version: str, refs=None):
        self.group = group
        self.version = version
        self.refs = refs

    @classmethod
    def from_matfile(cls, file_path: str):
        try:
            group = h5py.File(file_path, "r")
            refs = group["#refs#"]
            version = "h5"
        except OSError:
            group = sp.io.loadmat(file_path, struct_as_record=True, chars_as_strings=True)
            version = "loadmat"
            refs = None
        return cls(group=group, version=version, refs=refs)

    def __getitem__(self, item):
        if self.version == "h5":
            group = self.group[item]
        else:
            group = self.group[item][0][0]
        return self.__class__(group=group, version=self.version, refs=self.refs)


def convert_subtree(group: h5py.Group, refs: h5py.Group):
    """Converts everything in the group to dumb dicts / numpy arrays."""
    d = {}
    for key in group:
        if key == "#refs#":
            continue
        value = group[key]
        if isinstance(value, h5py.Group):
            d[key] = convert_subtree(value, refs=refs)
        elif isinstance(value, h5py.Dataset):
            d[key] = convert_dataset(value, refs=refs)
        else:
            raise ValueError(f"Can't convert {value} of type {type(value)}.")
    return d


def has_refs(dataset: h5py.Dataset):
    if len(dataset) == 0:
        return False
    if not isinstance(dataset[0], np.ndarray):
        return False
    if isinstance(dataset[0][0], h5py.h5r.Reference):
        return True
    return False


def convert_dataset(dataset: h5py.Dataset, refs: h5py.Group):
    """Convert h5py.dataset into python native datatypes according to the matlab class annotation"""
    # all MATLAB variables have the attribute MATLAB_class
    # if this is not present, it is not convertible
    if has_refs(dataset):
        mtype = "cell_with_refs"
    else:
        try:
            mtype = dataset.attrs["MATLAB_class"].decode()
        except KeyError:
            raise ValueError(f"{dataset} is not a MATLAB type.")

    if mtype == "cell_with_refs":
        cell = []
        for ref in dataset:
            row = []
            for r in ref:
                entry = convert_dataset(refs.get(r), refs=refs)
                row.append(entry)
            cell.append(row)
        return cell

    elif mtype == "char":
        if len(dataset) == 0:
            return ""
        elif isinstance(dataset[0], np.ndarray):
            return "".join([chr(x[0]) for x in dataset]).replace("\x00", "")
        else:
            return "".join([chr(x) for x in dataset]).replace("\x00", "")

    elif mtype == "bool":
        return bool(dataset)

    elif mtype == "logical":
        arr = np.array(dataset, dtype=bool).T.squeeze()
        if arr.size == 1:
            arr = bool(arr)
        return arr

    elif mtype == "canonical empty":
        return None

    # complex numbers need to be filtered out separately
    elif "imag" in str(dataset.dtype):
        if dataset.attrs["MATLAB_class"] == b"single":
            dtype = np.complex64
        else:
            dtype = np.complex128
        arr = np.array(dataset)
        arr = (arr["real"] + arr["imag"] * 1j).astype(dtype)
        return arr.T.squeeze()

    # if it is none of the above, we can convert to numpy array
    elif mtype in (
        "double",
        "single",
        "int8",
        "int16",
        "int32",
        "int64",
        "uint8",
        "uint16",
        "uint32",
        "uint64",
        "cell",
    ):
        if mtype == "cell":
            print(dataset)
        arr = np.array(dataset, dtype=dataset.dtype)
        return arr.T.squeeze()

    else:
        raise ValueError(f"Data type not supported: {mtype}, {dataset.dtype}.")


SHEET_ATTRS = (
        "category",
        "class",
        "code",
        "datatype",
        "descr",
        "entity",
        "name_category",
        "note",
        "scenario",
        "source",
        "subsource",
        "tablekind",
        "type",
        "unit",
    )


def primap_sheet_to_pandas(sheet: MatFileHandle):
    if sheet.version == "h5":
        # read from matlab v7.3+ style matfile, which is an hdf5 file
        attrs = {
            x: convert_dataset(sheet[f"sheet_{x}"].group, refs=sheet.refs) for x in SHEET_ATTRS
        }

        countries = np.array(convert_dataset(sheet["rowcodes_countries"].group, refs=sheet.refs)).flat
        years = np.array(sheet["colcodes_years"].group, dtype=np.uint16).flat

        data = sheet["data"].group
    else:
        # read from np.ndarray produced by scipy.io.loadmat
        attrs = {}
        for sheet_attr in SHEET_ATTRS:
            if sheet_attr == "subsource":
                attrs[sheet_attr] = sheet.group[f"sheet_{sheet_attr}"]
            else:
                attrs[sheet_attr] = sheet.group[f"sheet_{sheet_attr}"][0]

        countries = np.array(["".join(x) for x in sheet.group["rowcodes_countries"].flat])
        years = np.array(sheet.group["colcodes_years"].flat, dtype=np.uint16)

        data = sheet.group["data"]

    return attrs, pd.DataFrame(data=data, columns=countries, index=years)




class PRIMAPDB:
    @classmethod
    def from_mat(cls, file_path: str, progress=False, max_datatables=None):
        fh = MatFileHandle.from_matfile(file_path)

        # todo
        # self.category_tables = self._convert_subtree(self._h5["PRIMAPDB"]["category_tables"])
        # self.conversion_tables = self._convert_subtree(self._h5["PRIMAPDB"]["conversion_tables"])
        # self.country_table = self._convert_subtree(self._h5["PRIMAPDB"]["country_table"])
        # self.subcountry_table = self._convert_subtree(self._h5["PRIMAPDB"]["subcountry_table"])
        # self.source_table = self._convert_subtree(self._h5["PRIMAPDB"]["source_table"])

        ds = cls._convert_primapdb_sheet_collection_to_xarray_dataset(
            sheet_collection=fh["PRIMAPDB"]["mastertable"]["datatables"],
            progress=progress,
            max_datatables=max_datatables,
        )

        if fh.version == "h5":
            modified_by = cls._convert_dataset(fh["PRIMAPDB"]["modifiedBy"].group, refs=fh.refs)
            modified_at = datetime.datetime.strptime(
                cls._convert_dataset(fh["PRIMAPDB"]["modifiedOn"].group, refs=fh.refs), "%y%m%d_%H%M%S"
            )
            ds.attrs["modified_by"] = modified_by
            ds.attrs["modified_at"] = modified_at
        return cls(ds=ds, file_path=file_path)
