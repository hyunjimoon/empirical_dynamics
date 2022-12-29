
import matplotlib.pyplot as plt
import pandas as pd
from iter0 import get_data_path, get_plot_path, txt2df
import string

################ FED data
def hierarchize_org(time, features =['DATECODE','SALARY'], layers=5):
    """
    features: features from below to be tracked other than agnecy hierarchy five level ('AGYTYP', 'AGY', 'AGYSUB') e.g. SALARY
        # original data FACDATA.txt col" ['AGYSUB', 'LOC', 'AGELVL', 'EDLVL', 'GSEGRD', 'LOSLVL', 'OCC', 'PATCO',
    #          'PP', 'PPGRD', 'SALLVL', 'STEMOCC', 'SUPERVIS', 'TOA', 'WORKSCH',
    #          'WORKSTAT', 'DATECODE', 'EMPLOYMENT', 'SALARY', 'LOS', 'AGYTYP',
    #          'AGYTYPT', 'AGY', 'AGYT', 'AGYSUBT'] and by default it is organized into 1-4-130-530-1060 hierarchy

    layers: degree of fineness for organization hierarchy
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
    df = df.loc[:, features + ['AGYTYP', 'AGY', 'AGYSUB', 'is_mng']]
    df.rename(columns={'AGYTYP':'2AGYTYP', 'AGY': '3AGY','AGYSUB':'4AGYSUB','is_mng':'5is_mng'}, inplace=True)


    # if layers == 5:
    #     df = df[['AGYTYP', 'AGY', 'AGYSUB', 'is_mng']]
    #     df.columns = ['2AGYTYP', '3AGY', '4AGYSUB', '5is_mng']
    # elif layers == 4:
    #     df = df[['AGYTYP', 'AGY', 'AGYSUB']]
    #     df.columns = ['2AGYTYP', '3AGY', '4AGYSUB']
    # elif layers == 3:
    #     df = df[['AGYTYP', 'AGY']]
    #     df.columns = ['2AGYTYP', '3AGY']
    # elif layers == 2:
    #     df = df[['AGYTYP']]
    #     df.columns = ['2AGYTYP']

    # store plot
    # df_as = df.drop_duplicates('4AGYSUB')
    # df_as.groupby('3AGY')['4AGYSUB'].count().hist()
    # plt.savefig(f"{plot_path}/hist.png")

    #dft = pd.concat([dft, df], axis=1)
    df.to_pickle(f'{data_path}/{features}.pkl')
    return df

def constrcut_xarray():
    xr_lst = []
    for TIME_YEAR in TIME_YEARS:
        for TIME_MONTH in TIME_MONTHS:
            hierarchize_org(TIME_YEAR + TIME_MONTH, features)
            xr_lst.append(pd.read_pickle(get_data_path(f'agency/{TIME_YEAR + TIME_MONTH}') + f'/{features}.pkl').to_xarray())
    agency98_21 = xr.concat([xr for xr in xr_lst], dim = "index") #47m
    agency_bytime = agency98_21.groupby('DATECODE')
    # Q1.from decreasing agytyp mean, (categorized into four as 1: 'Cabinet Level Agencies':  2: 'Large Independent Agencies (1000 or more employees)':  (categorized to 1-4 dep on absolute size) mean
    # Q2.manager ratio peaked during 20s and is falling
    mng_ratio = agency_bytime.mean() # 5is_mng count is the number of employee of each agency at each year - how to plot?
    org_size = agency_bytime.count() # Employement count is the number of employee of each agency at each year - how to plot?


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

    sup = df.groupby("3AGY")['is_mng'].sum()
    tot = df.groupby("3AGY")['EMPLOYMENT'].count()
    suptot = pd.concat([sup, tot], axis=1)
    suptot["ratio"] = suptot["is_mng"] / suptot["EMPLOYMENT"]
    suptot[['EMPLOYMENT', 'ratio']].plot(kind='scatter', x='EMPLOYMENT', y='ratio', logx=True, logy=True)
    plt.savefig(f"{plot_path}/loglog_ratio_size.png")
    return