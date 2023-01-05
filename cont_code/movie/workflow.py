from util import * 
from iter import * 
import pandas as pd

def iter_title(iter, frac =1):
    set_dir_moviedata()
    iter_input =  {'forming_merge':'checking_out', 'checking_in_gane_eng':'forming_merge','forming_mutant_id':'checking_in_gane_eng','plotting':'forming_mutant_id'}
        
    if iter == 'preparing': #load data to use
        iter_preparing(iter, frac)

    elif iter == 'checking_out': #  "checking_out" DATA READ, CLEANING, OPT OUT SELECT ROWS
        iter_checking(iter_input[iter],iter)

    elif iter == 'forming_merge':
        iter_forming(iter_input[iter],iter)

    elif iter == 'checking_in_gane_eng': #SELECT ROWS: INFER title is ENG
        iter_checking(iter_input[iter],iter)
    
    elif iter == 'forming_mutant_id': #IDENTIFY MUTANT 
        iter_forming(iter_input[iter],iter)

    elif iter == 'plotting':
        iter_plotting(iter_input[iter],iter)


def iter_title_person():
    set_dir_moviedata()
    """
        DBTable('CompleteCast', #1.3m
            DBCol('id', INTCOL, notNone=True, alternateID=True),
            DBCol('movieID', INTCOL, index='idx_mid'),
            DBCol('subjectID', INTCOL, notNone=True, index='idx_sid'),
            DBCol('statusID', INTCOL, notNone=True)),
    """
    #old_title = pd.read_pickle("../data/movie/old_title.pkl")
    #old_person = pd.read_pickle("old_person.pkl")
    # old_title.columns = ['id', 'title','imdbIndex','kindID', 'year', 'imdbID',
    #                     'phoneticCode', 'episodeOfID', 'seasonNr', 'episodeNr', 'seriesYears', 'md5sum']

    new_person_name_movie = pd.read_pickle('new_person_basics.pkl')
    new_movie_person_character = pd.read_pickle('new_movie_principals.pkl')
    new_pm = pd.merge(new_person_name_movie, new_movie_person_character, on='nconst')
    np = new_pm[['nconst', 'tconst', 'category', 'characters']]
    pmc = np.loc[(np.category == 'actor') | (np.category == 'actress')] # 52m to 20m (1m movie - avg of 20?)
    pmc.to_pickle("new_person_movie_character.pkl")  # 52m

    return


def veva_title(df):
    """
    verification: consistency between imgrt and ntv
    validation: consistency check with cinemagoer
    """
    # sample titleid = tt_random.randint(1, 10145478)
    # get title, related person from cinemagoer
    # person = imdb(titleid).get_person()
    # TODO list of verification check
    # TODO list of validation check (compare with cinemagoer)
    # from imdb import Cinemagoer
    # ia = Cinemagoer()
    # movie = ia.get_movie('0856340')
    # print('Directors:')
    # for director in movie['directors']:
    #     print(director['name'])
    # # print the genres of the movie
    # print('Genres:')
    # for genre in movie['genres']:
    #     print(genre)
    # # search for a person name
    # people = ia.search_person('Mel Gibson')
    # for person in people:
    #    print(person.personID, person['name'])
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