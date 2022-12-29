from iter0 import set_dir_moviedata
from iter import sel_title, sel_year, sel_region, sel_rows_random, merge_title, save_iter, sel_region
import pandas as pd
import matplotlib.pyplot as plt

def combine_col2id(df):
    imgrt_ty = df.assign(
        imgrt_tyid =df.index.to_series().groupby(
            [df.title, df.year]
        ).transform('first').map('tyid{}'.format)
    )[['imgrt_tyid'] + df.columns.tolist()]
    return imgrt_ty

def veva_title2(df):
    """
    verification: consistency between imgrt and ntv
    validation: consistency with frank_list or cinemagoer
    """
    # sample titleid = tt_random.randint(1, 10145478)
    # get title, related person from cinemagoer
    # person = imdb(titleid).get_person()

    # TODO list of verification check

    # TODO list of validation check (compare with cinemagoer)
    return

def iter_preparing(ITER, frac):
    old_title = pd.read_csv('old_title.csv', keep_default_na=False, na_values=["NULL"])
    old_title.columns = ['id', 'title','imdbIndex','kindID', 'year', 'imdbID',
                         'phoneticCode', 'episodeOfID', 'seasonNr', 'episodeNr', 'seriesYears']#(, 'md5sum'])
    old_title = old_title.loc[:, ['title', 'year']]          

    new_title_aka = pd.read_csv('new_movie_akas.tsv', sep='\t', keep_default_na=False, na_values=["\\N"])
    new_title_basic = pd.read_csv('new_movie_basics.tsv', sep='\t', keep_default_na=False, na_values=["\\N"])
    new_title_basic = new_title_basic.rename(columns = {'originalTitle': 'title', 'startYear': 'year'}) 
    
    new_title_basic_cols = ['tconst', 'title', 'year', 'titleType'] # primaryTitle: 4.2m < originalTitle: 4.3m; going with originalTitle
    new_title_aks_cols = ['tconst',  'title', 'region']
    
    main = "outer"
    if main == "basic_major":
        new_title = pd.merge(new_title_basic[new_title_basic_cols], new_title_aka[new_title_aks_cols], on=('tconst', 'title' ), how = "left").loc[:, ['tconst', 'title', 'year', 'region', 'titleType']] #11m
    elif main == "outer": # primaryTitle: 4.2m < originalTitle: 4.3m; going with originalTitle
        new_title = pd.merge(new_title_basic[new_title_basic_cols], new_title_aka[new_title_aks_cols], on=('tconst', 'title'), how = "outer").loc[:, ['tconst', 'title', 'year', 'region', 'titleType']] #40m

    save_iter(sel_rows_random(old_title, frac=frac), ITER, is_imgrt = True) #imgrt_title.shape[0] 1.7m
    save_iter(sel_rows_random(new_title, frac=frac), ITER, is_imgrt = False) #ntv_title.shape[0] 10m

def iter_outing(ITER):
    old_title = pd.read_pickle('old_title.pkl')
    new_title = pd.read_pickle('new_title_ba_outer.pkl')

    imgrt_title = sel_year(sel_title(old_title, ITER), ITER)
    ntv_title = sel_year(sel_title(new_title, ITER, is_imgrt=False), ITER, is_imgrt=False)
    optout_nonus_ntv_title = sel_region(ntv_title) 

    save_iter(imgrt_title, ITER, is_imgrt = True) #imgrt_title.shape[0] 1.7m
    save_iter(optout_nonus_ntv_title, ITER, is_imgrt = False) #ntv_title.shape[0] 10m

def iter_merging(ITER_IN, ITER):
    imgrt_title = pd.read_pickle(f'{ITER_IN}_imgrt_title.pkl')
    ntv_title = pd.read_pickle(f'{ITER_IN}_ntv_title.pkl')

    mo = merge_title(combine_col2id(imgrt_title), ntv_title) #입국사무소통과후 원주민과 조인

    save_iter(mo, ITER)

def iter_ining_gane_eng(ITER_IN, ITER):
    mo = pd.read_pickle(f'{ITER_IN}' + ".pkl")

    mo_eng = sel_title(mo, ITER)  #sel_region(sel_title(mo, ITER)) 
    # sel_title(mo)[sel_title(mo).titleId.isnull()]: #77k -> 93k after making 가내수공업개발
    #mo_eng_usnull = mo_eng[(mo_eng.region == 'US') | mo_eng.region.isnull()] #3m
    # other ining criteria can exist -> ITER = '3ining_{cirteria}'
    save_iter(mo_eng, ITER) 

def iter_iding(ITER_IN, ITER):
    mo = pd.read_pickle(f'{ITER_IN}' + ".pkl")

    def separate_mutant_common_nativeEx(df):
        df.loc[df.tconst.isnull(), 'gene'] = 'mutant'
        df.loc[df.imgrt_tyid.isnull(), 'gene'] = 'native_ex'
        df.loc[(~df.imgrt_tyid.isnull()) & (~df.tconst.isnull()), 'gene'] = 'common'
        return df
    mo_mut_com_ne = separate_mutant_common_nativeEx(mo)
    # title-year duplicate: 173288
    # among title duplicates (600k), year+-1 difference:
    # 2,374,000 is unique title and after dropping year1 difference between imgrt-ntv, we would have 2.5m

    save_iter(mo_mut_com_ne, ITER)

def iter_plotting(ITER_IN, ITER):
    mo_mut_com_ne = pd.read_pickle(f'{ITER_IN}' + ".pkl")
    mutant = mo_mut_com_ne[mo_mut_com_ne.gene == 'mutant']
    mutant.year.hist()
    plt.savefig('mutant.png')
    #mutant.groupby('year').count().sort_values(by = 'index', ascending=False)
    save_iter(mutant, ITER)

def iter_title(iter, frac =1):
    set_dir_moviedata()
    iter_input =  {'2merging':'1outing', '3ining_gane_eng':'2merging','4iding_mutant':'3ining_gane_eng','5plotting':'4iding_mutant'}
        
    if iter == '0preparing': #load data to use
        iter_preparing(iter, frac)

    elif iter == '1outing': #  "1outing" DATA READ, CLEANING, OPT OUT SELECT ROWS
        iter_outing(iter)

    elif iter == '2merging':
        iter_merging(iter_input[iter],iter)

    elif iter == '3ining_gane_eng': #SELECT ROWS: INFER title is ENG
        iter_ining_gane_eng(iter_input[iter],iter)
    
    elif iter == '4iding_mutant': #IDENTIFY MUTANT 
        iter_iding(iter_input[iter],iter)

    elif iter == '5plotting':
        iter_plotting(iter_input[iter],iter)

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


if __name__ == "__main__":
    make_consistent_title()
