import xvec
from typing import Optional, Union

from openeo_processes_dask.process_implementations.data_model import VectorCube

__all__ = ["vector_reproject"]

def vector_reproject(
    data: VectorCube,
    projection: Optional[Union[str, int]] = None,
    dimension: Optional[str] = None,
) -> VectorCube:
    
    #TODO: add checks on the input data before proceeding
    #TODO: add handling of dimension parameter
    #TODO: projection input now works for strings like "EPSG:32628" but not for integer values like 32628, which is parsed as float instead of int

    geom_dim_name = data.to_dataarray().openeo.geometry_dims[0]
    return data.xvec.to_crs({geom_dim_name:projection})