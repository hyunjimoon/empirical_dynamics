import os

import matplotlib.pyplot as plt
import pandas as pd
from .match_format import get_data_path, get_plot_path, txt2df, set_dir_moviedata, set_dir_agencydata

################ IMDB data

def movie(old_columns = ['title', 'year'], new_columns = ['titleId', 'title', 'year', 'region', 'titleType'], main = "basic_major", frac = 1):
    """
    old_df: dataframe on imdb13 data
    new_df: dataframe on imdb13 data
    cut_num: int type row number to cut until
    characters: list of character to exclude
    """
    #os.chdir(os.getcwd() + "/data/movie")
    set_dir_moviedata()
    # old_movie = pd.read_pickle("../data/movie/old_title.pkl")
    # old_movie.columns = ['id', 'title','imdbIndex','kindID', 'year', 'imdbID',
    #                     'phoneticCode', 'episodeOfID', 'seasonNr', 'episodeNr', 'seriesYears', 'md5sum']

    # new_movie_aka = pd.read_pickle('new_movie_akas.pkl')
    # new_movie_basic = pd.read_pickle('new_movie_basics.pkl')
    # new_movie_basic = new_movie_basic.rename(columns = {"tconst": "titleId", 'originalTitle': 'title', 'startYear': 'year'})

    #new_movie_director = pd.read_pickle("data/imdb22/22title_crew.pkl")
    #newtitle_id.columns = ['titleId', 'directors', 'writers']

    # new_movie_basic_columns = ['titleId','primaryTitle', 'title', 'year', 'titleType']
    # new_movie_aks_colmns = ['titleId', 'region', 'title']
    # if main == "basic_major":
    #     new_movie = pd.merge(new_movie_basic[new_movie_basic_columns], new_movie_aka[new_movie_aks_colmns],   on=('titleId', 'title'), how = "left") #11m
    # elif main == "aka_major":
    #     new_movie = pd.merge(new_movie_basic[new_movie_basic_columns], new_movie_aka[new_movie_aks_colmns],   on=('titleId', 'title'), how = "right") #33m

    #old_movie.to_pickle("old_movie.pkl")
    #new_movie.to_pickle("new_movie.pkl")

    # FILTER ROWS
    #old_movie = pd.read_pickle('old_movie.pkl').loc[:, old_columns]
    new_movie = pd.read_pickle('new_movie.pkl').loc[:, new_columns] #f'{data_path}new_movie.pkl'

    # FILTER COLUMNS
    #old_movie, new_movie = filter_rows_random(old_movie, new_movie, frac=1) #.0001)


    #old_movie = filter_year(filter_title(old_movie))
    new_movie = filter_year(filter_title(filter_movie_others(new_movie), characters = ['Pilot', 'Finale']), is_old = False) # 169k
    #old_movie.to_pickle("old_movie_year_title.pkl")
    new_movie.to_pickle("new_movie_year_title_typemovie.pkl")
    return #old_movie, new_movie


def person(old_columns = ['id', 'name'] ):
#     """
#     1. compare old_person with new_person using name (only new data has born/death year?)
#     2.
#
#     **title.principals.tsv.gz** – Contains the principal cast/crew for titles
#
# -   tconst (string) - alphanumeric unique identifier of the title
# -   ordering (integer) – a number to uniquely identify rows for a given titleId
# -   nconst (string) - alphanumeric unique identifier of the name/person
# -   category (string) - the category of job that person was in
# -   job (string) - the specific job title if applicable, else '\N'
# -   characters (string) - the name of the character played if applicable, else '\N'
#     """

    set_dir_moviedata()
    old_person = pd.read_pickle("old_person.pkl")
    old_person.columns = ['id', 'name', 'imdbIndex', 'imdbId', 'gender', 'namePcodeCf', 'namePcodeNf', 'surnamePcode', 'md5sum']
    #old_person.columns = ['id', 'personID','infoTypeID','info', 'note']
    #                     'phoneticCode', 'episodeOfID', 'seasonNr', 'episodeNr', 'seriesYears', 'md5sum']

    new_person = pd.read_pickle('new_person_basics.pkl')
    new_person.rename(columns={'primaryName': 'name', 'birthYear': 'year'}, inplace=True)
    # new_movie_basic = pd.read_pickle('new_movie_basics.pkl')
    # new_movie_basic = new_movie_basic.rename(columns = {"tconst": "titleId", 'originalTitle': 'title', 'startYear': 'year'})

    #new_movie_director = pd.read_pickle("data/imdb22/22title_crew.pkl")
    #newtitle_id.columns = ['titleId', 'directors', 'writers']

    return old_person, new_person
def movie_person():
    set_dir_moviedata()
    """
        DBTable('CompleteCast', #1.3m
            DBCol('id', INTCOL, notNone=True, alternateID=True),
            DBCol('movieID', INTCOL, index='idx_mid'),
            DBCol('subjectID', INTCOL, notNone=True, index='idx_sid'),
            DBCol('statusID', INTCOL, notNone=True)),


    """
    old_movie = pd.read_pickle("../data/movie/old_title.pkl")
    old_person = pd.read_pickle("old_person.pkl")
    # old_movie.columns = ['id', 'title','imdbIndex','kindID', 'year', 'imdbID',
    #                     'phoneticCode', 'episodeOfID', 'seasonNr', 'episodeNr', 'seriesYears', 'md5sum']

    new_person_name_movie = pd.read_pickle('new_person_basics.pkl')
    new_movie_person_character = pd.read_pickle('new_movie_principals.pkl')
    new_pm = pd.merge(new_person_name_movie, new_movie_person_character, on='nconst')
    np = new_pm[['nconst', 'tconst', 'category', 'characters']]
    pmc = np.loc[(np.category == 'actor') | (np.category == 'actress')] # 52m to 20m (1m movie - avg of 20?)
    pmc.to_pickle("new_person_movie_character.pkl")  # 52m

    return


def filter_title(df, characters=['#', '-0', '-1']):
    """"
    series of title from which any title that include at least one elemnet of character would be filtered
    """

    df = df[~df.title.isnull()]
    # MOVIE
    for char in characters:
        df = df[~df['title'].str.contains(f"{char}", na=False)]  # 11k na for old title
    # PERSON
    return df


def filter_na(df, column):
    return df[~df.loc[: , column].isnull()]

def filter_year(df, is_old = True):
    # # OLD MOVIE
    if is_old:
        df = df[~df['year'].isnull()]
        df.year = df.year.astype('int')

    # # NEW MOVIE
    # df = df[~df['year'].isnull()]
    else:
        df = df[~df.year.isnull()]
        df.loc[:, 'year'] = df.year.apply(lambda x: int(x) if str(x).isnumeric() else -1)
        df = df[df.year > 0]# 170k
    # PERSON

    return df

def filter_movie_others(df, region = "US", titleType = "movie"):
    """
    language, region, genre (anything other than indexed title character and year)
    """
    df = df[(df['region'] == region) & (df['titleType'] == titleType)]
    #newtitle = newtitle[newtitle['language'] == "en"]
    return df


def filter_person_others(df, region = "US"):
    """
    characters other than title (name), year (identifier?) of person (actor) characterizing it
    """
    df = df[df['region'] == region]
    #newtitle = newtitle[newtitle['language'] == "en"]
    return df


def filter_rows_random(old_df, new_df, frac = 0.00001):
    return old_df.sample(frac = frac), new_df.sample(frac = frac)


def filter_columns(old_df, new_df, old_columns, new_columns):
    return old_df[old_columns], new_df[new_columns]


def join_movie(old_movie, new_movie):
    mi = pd.merge(old_movie, new_movie, on=('title', 'year'), how='inner')  # 600k
    mo = pd.merge(old_movie, new_movie, on=('title', 'year'), how='outer') # 2m
    mi.drop_duplicates(subset=['old_id', 'titleId'], keep='first', inplace=True, ignore_index=True)
    mo.drop_duplicates(subset=['old_id', 'titleId'], keep='first', inplace=True, ignore_index=True)
    mi.set_index('titleId', inplace = True)
    mo.reset_index(inplace = True)

    outer_columns = ['index', 'old_id', 'title', 'year', 'titleId']
    inner_columns = ['old_id', 'title', 'year']

    mo[outer_columns].to_csv("mo.tsv", sep='\t', index = False)
    mi[inner_columns].to_csv("mi.tsv", sep='\t')
    return


################ FED data
def hierarchize_org(time, features, layers = 5):
    """
    features: you wish to add e.g. salary level

    after merging fact with agy to groupby, it hierarchize according to `layers`.
    layer 5:                     SUPERVIS
    layer 4:                AGYSUB
    layer 3:              AGY
    layer 2:        AGYTYP
    layer 1: AGY_arch
    depending on analysis type, it filters columns
    """
    data_path = get_data_path(f'agency/{time}')
    plot_path = get_plot_path(f'agency/{time}')

    df_fact = txt2df(time, "FACTDATA")
    df_agy = txt2df(time, "DTagy")

    df = df_fact.merge(df_agy, on="AGYSUB")
    df = classify_layer(df, layer=5)
    dft = df.loc[:, features]
    # columnname is ['AGYSUB', 'LOC', 'AGELVL', 'EDLVL', 'GSEGRD', 'LOSLVL', 'OCC', 'PATCO',
    #          'PP', 'PPGRD', 'SALLVL', 'STEMOCC', 'SUPERVIS', 'TOA', 'WORKSCH',
    #          'WORKSTAT', 'DATECODE', 'EMPLOYMENT', 'SALARY', 'LOS', 'AGYTYP',
    #          'AGYTYPT', 'AGY', 'AGYT', 'AGYSUBT'] and we order them to 1-4-130-530-1060 hierarchy
    df.to_pickle(f'{data_path}/agency_hier_full.pkl')

    if layers == 5:
        df = df[['AGYTYP', 'AGY', 'AGYSUB', 'is_mng']]
        df.columns = ['2AGYTYP', '3AGY', '4AGYSUB', '5is_mng']
    elif layers == 4:
        df = df[['AGYTYP', 'AGY', 'AGYSUB']]
        df.columns = ['2AGYTYP', '3AGY', '4AGYSUB']
    elif layers == 3:
        df = df[['AGYTYP', 'AGY']]
        df.columns = ['2AGYTYP', '3AGY']
    elif layers == 2:
        df = df[['AGYTYP']]
        df.columns = ['2AGYTYP']

    # store plot
    df_as = df.drop_duplicates('4AGYSUB')
    df_as.groupby('3AGY')['4AGYSUB'].count().hist()
    plt.savefig(f"{plot_path}/hist.png")

    dft = pd.concat([dft, df], axis = 1)
    dft.to_pickle(f'{data_path}/agency_hier_{layers}_{features}.pkl')
    return dft


def classify_layer(df, layer):
    """
    we can have other classifications within layer 2, 3, 4 as well
    layer 2: 'Cabinet Level Agencies', 'Large Independent Agencies (1000 or more employees)', 'Medium Independent Agencies (100-999 employees)', 'Small Independent Agencies (less than 100 employees)'
    layer 3: AA - AF - ZU
    layer 4:
    layer 5:
    from {'*', '2', '4', '5', '6', '7', '8'}, 128 classification as numbers doesn't represent the level,
    considering 2,6,7 are supervisors
    """
    if layer == 5:
        df['is_mng'] = df["SUPERVIS"].isin(['2', '6', '7'])

    return df


def scale_plot(time):
    data_path = get_data_path(f'agency/{time}')
    plot_path = get_plot_path(f'agency/{time}')

    df = pd.read_pickle(f'{data_path}' + "/agency_hier_5_['SALARY', 'EMPLOYMENT'].pkl")

    sup = df.groupby("3AGY")['5is_mng'].sum()
    tot = df.groupby("3AGY")['EMPLOYMENT'].count()
    suptot = pd.concat([sup, tot], axis=1)
    suptot["ratio"] = suptot["5is_mng"] / suptot["EMPLOYMENT"]
    suptot[['EMPLOYMENT', 'ratio']].plot(kind='scatter', x='EMPLOYMENT', y='ratio', logx=True, logy=True)
    plt.savefig(f"{plot_path}/loglog_ratio_size.png")
    return

















