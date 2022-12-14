import os
import string
import pandas as pd
from iter0 import set_dir_moviedata
from simulation_test import make_consistent_title
import numpy as np
from imdb import Cinemagoer
import arviz as az
# import os
# os.chdir(os.getcwd() + "/data/movie")
# test data: old_movie = pd.read_pickle('data/movie/old_movie.pkl')
#set_dir_moviedata()
#make_consistent_title(frac =1)

# set_dir_moviedata()
# print(os.getcwd())

# iter0_ot = pd.read_pickle('old_title.pkl').loc[:, old_columns]
# iter0_nt = pd.read_pickle('new_title.pkl').loc[:, new_columns]
# iter1_mt = pd.read_pickle('iter1_merged_title.pkl')
# iter0_ot_xr = iter0_ot.to_xarray()
# print(iter0_ot_xr)

da = xr.DataArray(
    np.arange(6).reshape(2, 3), [("x", ["a", "b"]), ("y", [10, 20, 30])]
)
da
xr.concat([da.isel(y=slice(0, 1)), da.isel(y=slice(1, None))], dim="y")