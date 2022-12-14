import matplotlib.pyplot as plt
import pandas as pd
from langdetect import detect, DetectorFactory
DetectorFactory.seed = 0
from cont_code.movie.iter0 import get_data_path, get_plot_path, txt2df
import string

################ IMDB data

# TODO: @Dashadower how to design when input is differetn for each iter
def save_iter(df, iter, is_save, is_pkl, is_old):
    if is_save:
        if iter ==1:
            if is_old:
                if is_pkl:
                    df.to_pickle("iter1_old_title.pkl")
                else:
                    df.to_csv("iter1_old_title.tsv", sep='\t')
            else:
                if is_pkl:
                    df.to_pickle("iter1_new_title.pkl")
                else:
                    df.to_csv("iter1_new_title.tsv", sep='\t')

        elif iter ==2:
            if is_pkl:
                df.to_pickle("iter2_merged_title.pkl")
            else:
                df.to_csv("iter2_merged_title.tsv", sep='\t')
        elif iter == 3:
            if is_pkl:
                df.to_pickle("iter3_merged_title_eng_us_movie.pkl")
            else:
                df.to_csv("iter3_merged_title_eng_us_movie.tsv", sep='\t')
        elif iter == 4:
            if is_pkl:
                df.to_pickle("iter4_only_old_title.pkl")
            else:
                df.to_csv("iter4_only_old_title.tsv", sep='\t')

def compare_mental_material(df, iter, is_old=True): #TODO make this as writelines()
    # read out join in
    if iter == 1:
        if is_old:
            print("###### ITER1 read and optout sel COMPLETE\n", df.head())
        else:
            print(df)
    elif iter == 2:
        print("###### ITER2 join COMPLETE")
        print("rows with titleId should include nonenglish term\n", df.head())
    elif iter == 3:
        print("###### ITER3 optin sel COMPLETE\n")
        print("new_movie deleted na year and include nonmovie type and non us region, nonenglish titiles", df.head())
    elif iter == 4:
        print("###### ITER4 set difference COMPLETE\n")
        print("new_movie deleted na year and include nonmovie type and non us region, nonenglish titiles", df.head())

def sel_title(df, iter, characters=['#', '-0', '-1'], is_old = True):
    """"
    series of title from which any title that include at least one elemnet of character would be filtered
    iter:1 quick, dirty, opt-out way preprocessing
    iter:2 detailed e.g. title language, more crafty, opt-in way preprocessing
    """
    if iter ==1:
        df = df[~df.title.isnull()]
        for char in characters:
            df = df[~df['title'].str.contains(f"{char}", na=False)]  # 11k na for old title
    # 1.8m old, #1687553 is Ajeossi
    elif iter ==2:
        # english sytax: consists of alphabet + numbers
        df['soft_eng'] = df.title.apply(lambda x: is_english(x))
        df = df[df.soft_eng == True]

    elif iter == 3:
        # english semantic: consists of alphabet + numbers
        df['strong_eng'] = df.title.apply(lambda x: detect(x)) #"Anajigoku" pass iter2, fail iter3 (sw)
        df = df[df.strong_eng == True]
   
    return df

def sel_year(df, iter, is_old = True):
    """"
    series of title from which any title that include at least one elemnet of character would be filtered
    iter:1 WEAK quick, dirty, opt-out way preprocessing for merging old and new
    iter:2 STRONG detailed e.g. title language, more crafty, opt-in  preprocessing
    """
    if iter == 2:
        if is_old:
            df = df[~df['year'].isnull()]
            df.year = df.year.astype('int')
        else:
            df = df[~df.year.isnull()]
            df.loc[:, 'year'] = df.year.apply(lambda x: int(x) if str(x).isnumeric() else -1)
            df = df[df.year > 0] # 170k
    elif iter == 3:
        raise NotImplementedError
        # # MOVIE by year
        # df = df[df.year == year]
    return df

def sel_region_type(df, region = "US", titleType = "movie"):
    """
    language, region, genre (anything other than indexed title character and year)
    """
    df = df[(df['region'] == region) & (df['titleType'] == titleType)]
    #newtitle = newtitle[newtitle['language'] == "en"]
    return df


def sel_person_others(df, region = "US"):
    """
    characters other than title (name), year (identifier?) of person (actor) characterizing it
    """
    df = df[df['region'] == region]
    #newtitle = newtitle[newtitle['language'] == "en"]
    return df


def sel_rows_random(old_df, new_df, frac = 0.00001):
    return old_df.sample(frac = frac), new_df.sample(frac = frac)


def join_movie(old_movie, new_movie, is_save):
    # mi = pd.merge(old_movie, new_movie, on=('title', 'year'), how='inner')  # 600k
    # mi.drop_duplicates(subset=['old_id', 'titleId'], keep='first', inplace=True, ignore_index=True)
    # mi.set_index('titleId', inplace=True)
    inner_columns = ['old_id', 'title', 'year']
    # if is_save:
        #mi[inner_columns].to_csv("mi.tsv", sep='\t')

    mo = pd.merge(old_movie, new_movie, on=('title', 'year'), how='outer') # 2m

    #print(mo.shape[0]) # 10m
    mo.to_csv("mo_1207.tsv", sep = '\t') # drop
    mo.drop_duplicates(subset=['old_id', 'titleId'], keep='first', inplace=True, ignore_index=True)
    #print(mo.shape[0])# 10m
    mo.reset_index(inplace = True)
    outer_columns = ['index', 'old_id', 'title', 'year', 'titleId']

    if is_save:
        mo[outer_columns].to_csv("mo.tsv", sep='\t', index = False)

    return mo


def is_english(word):
    """
    is_english("A few good mand 2", "Wall-e") True
    """
    eng_charc = f"{string.ascii_lowercase + string.ascii_uppercase}" + " 0123456789" + "!-@#$%&*()/?+ "
    return len(set([i for i in word] + [e for e in eng_charc])) == 52 + 10 + 14

# def make_title_lang(df, is_old=False, is_save=False):
#     df['soft_eng'] = df.title.apply(lambda x: is_english(x))
#     if is_save:
#         if is_old:
#             df.to_pickle("old_movie_lang.pkl")
#         else:
#             df.to_pickle("new_movie_lang.pkl")
#     print("from make_title_lang", "length: ", df.shape[0], df.head())
#     return

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

















