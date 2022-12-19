import os
import pandas as pd
import random
import string
random.seed(100)


def get_plot_path(model_name):
    plot_path = f"../plot/{model_name}/"
    if not os.path.exists(plot_path):
        os.makedirs(plot_path)
    return plot_path


def get_data_path(model_name):
    data_path = f"../data/{model_name}/"
    if not os.path.exists(data_path):
        os.makedirs(data_path)
    return data_path

def txt2df(time, filename):
    data_path = get_data_path(f'fed_orig/{time}')
    if filename == "FACTDATA":
        if time[-2:] == "12":
            filename = filename + "_DEC" + time[:4]
        elif time[-2:] == "09":
            filename = filename + "_SEP" + time[:4]
    df = pd.read_csv(f"{data_path}{filename}.txt", header=0, low_memory=False)
    # df.to_xarray().to_netcdf(f"{filename[:-4]}.nc")
    # nc_loc = []
    # nc_loc += filename[:-4] + ".nc"
    # return nc_loc
    return df

def set_dir_agencydata():
    os.chdir(os.getcwd() + "/data/agency")

def pd_set_display():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    pd.set_option('display.colheader_justify', 'center')
    pd.set_option('display.precision', 2)
