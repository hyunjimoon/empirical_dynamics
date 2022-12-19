from iter0 import set_dir_moviedata
from iter import sel_title, sel_year, sel_region, sel_titleType, sel_rows_random, join_movie, save_iter, compare_mental_material
import pandas as pd
import matplotlib.pyplot as plt


def print_shape(old, new):
    return old.shape[0], new.shape[0]


def combine_col2id(df):
    test = df.assign(
        old_id =df.index.to_series().groupby(
            [df.title, df.year]
        ).transform('first').map('OLD{}'.format)
    )[['old_id'] + df.columns.tolist()]
    return test

def veva_title(df):
    """
    verification: consistency between old and new
    validation: consistency with frank_list or cinemagoer
    """
    # sample titleid = tt_random.randint(1, 10145478)
    # get title, related person from cinemagoer
    # person = imdb(titleid).get_person()

    # TODO list of verification check

    # TODO list of validation check (compare with cinemagoer)
    return


def veva_person(df):
    # """
    # given old and new dataframe with person name, old_id (old) and person name, birthyear, new_id (new),
    # returns 1. unified union dataframe with person name, id, person name, birthyear
    #         2. map of (old_id, union_id), (new_id, union_id)

    # #     1. compare old_person with new_person using name (only new data has born/death year?)
    # #     **title.principals.tsv.gz** – Contains the principal cast/crew for titles
    # # -   tconst (string) - alphanumeric unique identifier of the title
    # # -   ordering (integer) – a number to uniquely identify rows for a given titleId
    # # -   nconst (string) - alphanumeric unique identifier of the name/person
    # # -   category (string) - the category of job that person was in
    # # -   job (string) - the specific job title if applicable, else '\N'
    # # -   characters (string) - the name of the character played if applicable, else '\N'
    # """

    old_columns = ['id', 'name']
    set_dir_moviedata()
    old_person = pd.read_pickle("old_person.pkl")
    old_person.columns = ['id', 'name', 'imdbIndex', 'imdbId', 'gender', 'namePcodeCf', 'namePcodeNf', 'surnamePcode',
                          'md5sum']
    # old_person.columns = ['id', 'personID','infoTypeID','info', 'note']
    #                     'phoneticCode', 'episodeOfID', 'seasonNr', 'episodeNr', 'seriesYears', 'md5sum']

    new_person = pd.read_pickle('new_person_basics.pkl')
    new_person.rename(columns={'primaryName': 'name', 'birthYear': 'year'}, inplace=True)
    # new_movie_basic = pd.read_pickle('new_movie_basics.pkl')
    # new_movie_basic = new_movie_basic.rename(columns = {"tconst": "titleId", 'originalTitle': 'title', 'startYear': 'year'})

    # new_movie_director = pd.read_pickle("data/imdb22/22title_crew.pkl")
    # newtitle_id.columns = ['titleId', 'directors', 'writers']

    return old_person, new_person


def make_consistent_title(old_columns = ['title', 'year'], new_columns = ['titleId', 'title', 'year', 'region', 'titleType'], frac =1, IS_SAVE = True, IS_PKL = True):
    idata_lst = []
    ##################################################################################
    ## ITER 1: DATA READ, CLEANING, OPT OUT SELECT ROWS ####################
    ##################################################################################
    ITER = 'optout'
    set_dir_moviedata()
    #prepare_title_data(IS_SAVE)

    # SELECT COLUMNS
    # old_movie = pd.read_pickle('old_title.pkl').loc[:, old_columns]
    # new_movie = pd.read_pickle('new_title.pkl').loc[:, new_columns]
    old_movie = pd.read_pickle('old_title.pkl').loc[:, old_columns]
    new_movie = pd.read_pickle('new_title.pkl').loc[:, new_columns]
    old_movie, new_movie = sel_rows_random(old_movie, new_movie, frac=frac) #.00001

    old_movie = sel_year(sel_title(old_movie, ITER), ITER)
    new_movie = sel_year(sel_title(new_movie, ITER, is_old=False), ITER, is_old=False)
    save_iter(old_movie, ITER, IS_SAVE, IS_PKL, is_old = True) #old_movie.shape[0] 1.7m
    save_iter(new_movie, ITER, IS_SAVE, IS_PKL, is_old = False) #new_movie.shape[0] 10m
    #compare_mental_material(old_movie, ITER)
    #compare_mental_material(new_movie, ITER, is_old=False)

    ##################################################################################
    ## ITER 2: JOIN
    ##################################################################################
    ITER = 'join'
    # TODO sel_title old_movie before or after merge? (if justifiable, the more the better for old)

    # JOIN OLD NEW
    mo = join_movie(combine_col2id(old_movie), new_movie, is_save=IS_SAVE)
    save_iter(mo, ITER, IS_SAVE, IS_PKL)
    compare_mental_material(new_movie, ITER, is_old=False)

    ##################################################################################
    ## ITER 3: OPT IN SELECT ROWS: INFER title is ENG or then select US region
    ##################################################################################
    ITER = 'optin_ganesugong_eng'
    mo_eng = sel_title(mo, ITER)  #sel_region(sel_title(mo, ITER)) 
    # sel_title(mo)[sel_title(mo).titleId.isnull()]: #77k -> 93k after making 가내수공업개발
    # sel_region_type(sel_title(mo))[sel_region_type(sel_title(mo)).titleId.isnull()]: 0
    save_iter(mo_eng, ITER, IS_SAVE, IS_PKL)
    compare_mental_material(mo_eng, ITER, is_old=True)

    #mo_eng_us_movie = sel_titleType(mo_eng_us_movie)

    ##################################################################################
    ## ITER 4: SET DIFFERENCE
    ##################################################################################
    ITER = 'diff'
    old_only = mo_eng[mo_eng.titleId.isnull()]
    old_only.year.hist()
    plt.savefig('old_not_new.png')
    old_only.groupby('year').count().sort_values(by = 'index',ascending=False)
    save_iter(old_only, ITER, IS_SAVE, IS_PKL)
    #compare_mental_material(new_movie, ITER, is_old=True)
    # print compare
    return


def make_consistent_title_person():
    set_dir_moviedata()
    """
        DBTable('CompleteCast', #1.3m
            DBCol('id', INTCOL, notNone=True, alternateID=True),
            DBCol('movieID', INTCOL, index='idx_mid'),
            DBCol('subjectID', INTCOL, notNone=True, index='idx_sid'),
            DBCol('statusID', INTCOL, notNone=True)),
    """
    #old_movie = pd.read_pickle("../data/movie/old_title.pkl")
    #old_person = pd.read_pickle("old_person.pkl")
    # old_movie.columns = ['id', 'title','imdbIndex','kindID', 'year', 'imdbID',
    #                     'phoneticCode', 'episodeOfID', 'seasonNr', 'episodeNr', 'seriesYears', 'md5sum']

    new_person_name_movie = pd.read_pickle('new_person_basics.pkl')
    new_movie_person_character = pd.read_pickle('new_movie_principals.pkl')
    new_pm = pd.merge(new_person_name_movie, new_movie_person_character, on='nconst')
    np = new_pm[['nconst', 'tconst', 'category', 'characters']]
    pmc = np.loc[(np.category == 'actor') | (np.category == 'actress')] # 52m to 20m (1m movie - avg of 20?)
    pmc.to_pickle("new_person_movie_character.pkl")  # 52m

    return


if __name__ == "__main__":
    make_consistent_title()
