import matplotlib.pyplot as plt
import pandas as pd
from iter0 import get_data_path, get_plot_path, txt2df
import string


################ IMDB data

# TODO: @Dashadower how to design when input is differetn for each iter
def save_iter(df, iter, is_save, is_pkl, is_old = False):
    if is_save:
        if iter == 'optout':
            if is_old:
                df.to_pickle("1optout_old_title.pkl")
            else:
                df.to_pickle("1optout_new_title.pkl")
        elif iter == 'join':
            if is_pkl:
                df.to_pickle("2join_merged_title.pkl")
            else:
                df.to_csv("2join_merged_title.tsv", sep='\t')
        elif iter == 'optin_ganesugong_eng':
            if is_pkl:
                df.to_pickle("3opting_merged_title_eng_movie.pkl")
                df.set_index('titleId').to_xarray().to_netcdf("3opting_merged_title_eng_movie.nc")
            else:
                df.to_csv("3opting_merged_title_eng_movie.tsv", sep='\t')
        elif iter == 'diff':
            if is_pkl:
                df.to_pickle("4diff_only_old_title.pkl")
                df.set_index('titleId').to_xarray().to_netcdf("4diff_only_old_title.nc")
            else:
                df.to_csv("4diff_only_old_title.tsv", sep='\t')


def compare_mental_material(df, iter, is_old=True):  # TODO make this as writelines()
    if iter == 'optout':
        if is_old:
            print("###### ITER optout COMPLETE\n", df)
        else:
            print(df)
    elif iter == 'join':
        print("###### ITER join COMPLETE")
        print("from merged table, only old's `titleId` is na, only new's `old_id`is na", df)
        print("rows with titleId should include nonenglish term\n", df)

    elif iter == 'optin_ganesugong_eng' or iter == 'optin_opensource_eng':
        print("###### ITER optin COMPLETE\n")
        print("new_movie deleted na year + nonmovie type and non us region, nonenglish titiles", df)


def sel_title(df, iter, is_old=True):
    """"
    series of title from which any title that include at least one elemnet of character would be filtered
    iter:1 quick, dirty, opt-out way preprocessing
    iter:2 detailed e.g. title language, more crafty, opt-in way preprocessing
    """
    if iter == 'optout':
        df = df[~df.title.isnull()]  # 11k na for old title, 0 na for new title
        if is_old:
            for char in ['#', '-0', '-1', 'Final', 'Pilot']:
                df = df[~df['title'].str.contains(f"{char}", na=False)]
        else:
            for char in ['Final', 'Pilot']:
                df = df[~df['title'].str.contains(f"{char}", na=False)]
                # 11,578,172 -> 11,555,926 (optout Final), 11,545,080 (optout Pilot)
    elif iter == 'optin_ganesugong_eng':
        df['soft_eng'] = df.title.apply(lambda x: is_english(x))
        df = df[df.soft_eng == True]

    elif iter == 'optin_opensource_eng': #detect("Overdrive") # not very precise
        raise NotImplementedError

        #df['strong_eng'] = df.title.apply(lambda x: detect(x))  # "Anajigoku" pass iter2, fail iter3 (sw)
        df = df[df.strong_eng == 'en']

    return df


def sel_year(df, iter, is_old=True):
    """"
    series of title from which any title that include at least one elemnet of character would be filtered
    iter:1 WEAK quick, dirty, opt-out way preprocessing for merging old and new
    iter:2 STRONG detailed e.g. title language, more crafty, opt-in  preprocessing
    """
    if iter == 'optout':
        if is_old:
            df = df[~df['year'].isnull()]
            df.year = df.year.astype('int')
        else:
            df = df[~df.year.isnull()]
            df.loc[:, 'year'] = df.year.apply(lambda x: int(x) if str(x).isnumeric() else -1)
            df = df[df.year > 0]  # 170k
    elif iter == 'optin_ganesugong_eng' or iter == 'optin_opensource_eng':
        raise NotImplementedError
        # # MOVIE by year
        # df = df[df.year == year]
    return df


def sel_region(df, region="US"):
    return  df[df['region'] == region]


def sel_titleType(df, titleType="movie"):
    return  df[df['titleType'] == titleType]



def sel_person_others(df, region="US"):
    """
    characters other than title (name), year (identifier?) of person (actor) characterizing it
    """
    df = df[df['region'] == region]
    # newtitle = newtitle[newtitle['language'] == "en"]
    return df


def sel_rows_random(old_df, new_df, frac=0.00001):
    return old_df.sample(frac=frac), new_df.sample(frac=frac)


def join_movie(old_movie, new_movie, is_save):
    # mi = pd.merge(old_movie, new_movie, on=('title', 'year'), how='inner')  # 600k
    # mi.drop_duplicates(subset=['old_id', 'titleId'], keep='first', inplace=True, ignore_index=True)
    # mi.set_index('titleId', inplace=True)
    inner_columns = ['old_id', 'title', 'year']
    # if is_save:
    # mi[inner_columns].to_csv("mi.tsv", sep='\t')
    print(old_movie)
    print(new_movie)
    mo = pd.merge(old_movie, new_movie, on=('title', 'year'), how='outer')  # 2m

    # # print(mo.shape[0]) # 10m
    # mo.to_csv("mo_1207.tsv", sep='\t')  # drop
    mo.drop_duplicates(subset=['old_id', 'titleId'], keep='first', inplace=True, ignore_index=True)
    # print(mo.shape[0])# 10m
    mo.reset_index(inplace=True)
    outer_columns = ['index', 'old_id', 'title', 'year', 'titleId']

    if is_save:
        mo[outer_columns].to_csv("mo.tsv", sep='\t', index=False)

    return mo


def is_english(word):
    """
    the followings are TRUE
    # exclude: 4½, 11½, 39 ½, ¡1990!, 3... 2... 1, 
    # include: +0043-,22:43,31,<--->, 9-9-81,2011 03 19,9/11,(___),00:10, 50-50, 1/2, 0300 - 0430,
                    "A few good man 2", "Wall-e", "9:00""9:00", "What Is God's Eternity?", "W@anker"
    "angie';;;kdoi#422s anger <--->$400,000(2013,00,1875,1980,1981,11/11/11,11/11/11,11/11/11,199,355,99,7211,1,8,065,270,W@anker,09.12.04.,'77,285,092,1996,1974
        "A few good man 2", "Wall-e", "9:00""9:00", "What Is God's Eternity?", "W@anker"
    "angie';;;kdoi#422s anger <--->$400,000(2013,00,1875,1980,1981,11/11/11,11/11/11,11/11/11,199,355,99,7211,1,8,065,270,W@anker,09.12.04.,'77,285,092,1996,1974
    
    # 505,1993,324,4½,11½,329,1988,1988,161,067,141,12:21,$9.99,00:01:18,241,8/10000,422,1997,1.52,2@2,81,1/365,3,008, 5,251,024,027,3:19,600 - 115,010,
    # $600,000,$600,000,24/7,234,215,487,332,332,1-9,7/8,22:43,31,
    # 9:03, 145, 063, 30 1/2, 5:55, 3+1=1, 15:30:03, 180, 999, 422, 271, 107,107,315,12,02,100%,235,86,009,1.60,$1.11,19., 115,15,290,4.0,555
    # 4.0,555,<--->,457,1962,118,11,339,010101,18,50,$1,000,000,$1,000,000,266,3601,2001,5,249,054,025,1945,248,304
    # $300,000, $300,000,$300,000,$300,000,$300,000
    # 377, 154,1984,1984,1981,1992,1992,341,295,344,1+1=2,1+1+1,259,45,09:21:25,059,111,165,129,450,20/2/1991,
    # 8,08/15,307,8,$200,000,$200,000,148,4,4,4,12:00,424,7002,299,299,427,427,$400,000,$400,000,$400,000,$400,000,$400,000
    # $1,000,000,48,109,3:18,1973,1973,251,301,301,301,10.09.09,360 º,69,102,323,220,71,13:30,402,13:04,$3.52,47,26,1:0,26/9 1994,230,461,020,
    # 1918,1998,1998,$900,000,$900,000,25/01/95,1930,50/50,Chantal@avro.nl,1821,1821,077,1.65,100,29,3461,'49-'17,326,1567 - 1568,460,214,1950,
    # (2013,00,1875,1980,1981,11/11/11,11/11/11,11/11/11,199,355,99,7211,1,8,065,270,W@anker,09.12.04.,'77,285,092,1996,1974
    # 179, "301, 302",1968,1968,120,(2004,Ded@ns,26/9/1991,2184,25,405,1505,070,1992,1992,1972,49?,"5, 10, 15"
    # $400,000,156,0,999,42,911,217,11:11,114,114,1988,1987,1987,"0,08", 103109,2011 05 26,5,5,5,410,410,1.56,52,52,531,1949- 1959,00.000,50,76,142,
    # 66,50-50,8:00,789,10-57,2012,2012,2012,2012,2012,84,312,4.255,1915,10:10,25/7,541-69-96,5/31,103,20:10,201,2+2=3,73,73,19,100,1982,39,Midnatt@nrk,411,1974,80,1983,1983,11:50,
    # 4:37,1993,1993,1893,19084,322,322,1977,1977,22,342,2+1,091,105,105,207,1:42.08,10:00,1968,326,126,2038,8090,'11',2/16/12,238,3187345,206,1997,1997,19-2,¡1990!,(2012,6500,
    # 120,$,325,1674,23,88,2012,2012,42 1/2, 32, 1/3,10:48,22,22,1959,094,22:22,40,40,218,157,16/9/1991,474,101,79,.73, 2012,2012,2012,2012,725,173,344,5,5,5,5,
    # 1978,302,119,87,080,1.33,977,1.51,1925,21,167,500 & 5,14,69,155,1968,1968,+0043-,$300,000,$300,000,$300,000,$300,000, 1/20,183,2011 03 19, 24/604, 1978, 9:00, 066, (1972

    """
    eng_charc = f"{string.ascii_lowercase + string.ascii_uppercase}" + "0123456789" + " !_-=@#$%&*()/?+:;.,$<>" + "'"
    return len(set([i for i in word] + [e for e in eng_charc])) == 52 + 10 + 23


# def make_title_lang(df, is_old=False, is_save=False):
#     df['soft_eng'] = df.title.apply(lambda x: is_english(x))
#     if is_save:
#         if is_old:
#             df.to_pickle("old_movie_lang.pkl")
#         else:
#             df.to_pickle("new_movie_lang.pkl")
#     print("from make_title_lang", "length: ", df.shape[0], df.head())
#     return


