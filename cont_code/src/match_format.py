import os

import pandas as pd
import random
import string
random.seed(100)
# source
DATA_LOC = "data/"
DATA_SOURCE = "imdb/"
DATA_SOURCE = "fed/"
TIME_YEAR = "21"
TIME_MONTH = "09"

LOC = DATA_LOC + DATA_SOURCE + TIME_YEAR + "_"  + TIME_MONTH

def get_plot_path(model_name):
    plot_path = f"plot/{model_name}/"
    if not os.path.exists(plot_path):
        os.makedirs(plot_path)
    return plot_path


def get_data_path(model_name):
    data_path = f"data/{model_name}/"
    if not os.path.exists(data_path):
        os.makedirs(data_path)
    return data_path


def csv2pkl():
    filepath = "data"
    df17_name = pd.read_csv(filepath + "/imdb13/name.csv")
    df17_title = pd.read_csv(filepath + "/imdb13/title.csv")
    df17_cast = pd.read_csv(filepath + "/imdb13/cast_info.csv")
    df22_name = pd.read_csv(filepath + "/imdb22/name.basics.tsv", sep='\t')
    df22_crew = pd.read_csv(filepath + "/imdb22/title.crew.tsv", sep='\t')

    df17_name.to_pickle("/imdb13/17name.pkl")
    df17_title.to_pickle("/imdb13/17title.pkl")
    df17_cast.to_pickle("/imdb22/17cast.pkl")
    df22_name.to_pickle("/imdb22/22name.pkl")
    df22_crew.to_pickle("/imdb22/22crew.pkl")

    # list of existing data
    file_lst13 = ["keyword", "aka_name", "aka_title", "char_name", "movie_info", "movie_link", "person_info",
                  "complete_cast", "movie_keyword", "movie_info_idx", "movie_companies"]

    file_lst22 = ["actor_name", "movie_crew", "movie_ratings", "movie_principals", "movie_episode", "movie_akas"]

def txt2df(time, filename):
    data_path = get_data_path(f'fed/{time}')

    df = pd.read_csv(f"{data_path}/{filename}.txt", header=0, low_memory=False)
    # df.to_xarray().to_netcdf(f"{filename[:-4]}.nc")
    # nc_loc = []
    # nc_loc += filename[:-4] + ".nc"
    # return nc_loc
    return df

def make_pkl13(flie_lst):
    filepath = "../data"
    for file in flie_lst:
        df = pd.read_csv(f"{filepath}/imdb13/{file}.csv")
        df.to_pickle(f"{filepath}/imdb13/{file}.pkl")


def make_pkl22(flie_lst):
    filepath = "../data"
    for file in flie_lst:
        df = pd.read_csv(f"{filepath}/imdb22/{file}.tsv", sep='\t')
        df.to_pickle(f"{filepath}/imdb22/{file}.pkl")

def pkl2dict(year, file_lst):
    df_dict = dict() #
    for key in file_lst:
        df_dict[f'{year}_{key}']=pd.read_pickle(f"data/imdb{year}/{key}.pkl")
    return df_dict

def df2actor(df, year_from = 1900, year_to = 2030):
    """
    df: full data with eight columns
    year_from_to: e.g. (1940, 2000)
    """
    df = df[(df.ReleaseYear > year_from) & (df.ReleaseYear < year_to)]
    spl_char = ", "
    test_list = df.Stars.apply(lambda x: x.split(spl_char))
    actors = list(zip(*test_list))
    print(actors)
    return actors


def is_english(word):
    eng_charc = f"{string.ascii_lowercase + string.ascii_uppercase}" + " 0123456789" + "!@#$%&*()?+"
    return len(set([i for i in word] + [e for e in eng_charc])) == 52 + 11 + 11

####### DEPRECATED
# def read_tsv(filename):
#     ans = []
#     # open .tsv file
#     with open(f"{filename}.tsv") as f:
#
#         # Read data line by line
#         for line in f:
#             # split data by tab
#             # store it in list
#             l = line.split('\t')
#
#             # append list to ans
#             ans.append(l)
#
#     # print data line by line
#     for i in ans:
#         print(i)
#     return


# def title(old_columns, new_columns):
#     """
#     old_df: dataframe on imdb13 data
#     new_df: dataframe on imdb13 data
#     cut_num: int type row number to cut until
#     characters: list of character to exclude
#     """
#     oldtitle = pd.read_pickle("data/imdb13/13title.pkl")
#     newtitle_id = pd.read_pickle("data/imdb22/22title_crew.pkl")
#     newtitle_name = pd.read_pickle('data/imdb22/22movie_akas.pkl')
#
#     oldtitle.columns = ['id', 'title','imdbIndex','kindID', 'productionYear', 'imdbID',
#                         'phoneticCode', 'episodeOfID', 'seasonNr', 'episodeNr', 'seriesYears', 'md5sum']
#
#     newtitle_id.columns = ['titleId', 'directors', 'writers']
#
#     newtitle = pd.merge(newtitle_id, newtitle_name, on = "titleId", )
#
#     oldtitle[old_columns].to_pickle("analysis/data/imdb13/oldtitle.pkl")
#     newtitle[new_columns].to_pickle("analysis/data/imdb22/newtitle.pkl")
#     return



def pd_set_display():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    pd.set_option('display.colheader_justify', 'center')
    pd.set_option('display.precision', 2)


def tsv2df(file_name):
    df = pd.read_csv(f'data/imdb22/{file_name}.tsv', on_bad_lines='skip', sep='\t')
    df.to_pickle(f'data/imdb22/{file_name}.pkl')
    return df


if __name__ == "__main__":
    print("main")
    # old_df, new_df = filter(["#", "!", "-0"])
    # old_df, new_df = test(old_df, new_df, cut_num)
    # title_compare(old_df, new_df)
    