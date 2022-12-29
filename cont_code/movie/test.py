import os
import xarray as xr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker

from iter0 import set_dir_moviedata
from iter import sel_title, sel_year, sel_region, sel_rows_random, merge_title, save_iter, sel_region
from simulation_test import veva_person, iter_title, iter_title_person

# test data: old_movie = pd.read_pickle('data/movie/old_movie.pkl')
set_dir_moviedata()
#make_consistent_title(frac =.000001)
#iter1_old = pd.read_pickle('iter2_merged_title_full.pkl')
# TBC netcdf attempts
# optin3 = xr.open_dataset("3opting_merged_title_eng_movie.nc")
# old_only4 = xr.open_dataset("4diff_only_old_title.nc")

for iter in ['0preparing', '1outing', '2merging', '3ining_gane_eng', '4iding_mutant', '5plotting']:
    iter_title(iter, frac =.0001)