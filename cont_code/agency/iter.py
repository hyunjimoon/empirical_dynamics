import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.mixture import GaussianMixture
from util import *

def iter_preparing(time_lst, feature, ITER):
    """
    extract features to form nested data 
    layer 2: 'Cabinet Level Agencies', 'Large Independent Agencies (1000 or more employees)', 'Medium Independent Agencies (100-999 employees)', 'Small Independent Agencies (less than 100 employees)'
    layer 3: AA - AF - ZU
    from {'*', '2', '4', '5', '6', '7', '8'}, acc.to doc, 2,6,7 are supervisors
    """
    df_lst = []
    for time in time_lst:
        df_fact = txt2df(time, "FACTDATA")
        df_agy = txt2df(time, "DTagy")
        df = df_fact.merge(df_agy, on="AGYSUB")
        df = branching(df, branch='mng')
        df = df.loc[:, feature + ['AGYTYP', 'AGY', 'AGYSUB', 'is_mng']]
        df.rename(columns={'AGYTYP':'2AGYTYP', 'AGY': '3AGY','AGYSUB':'4AGYSUB','is_mng':'5is_mng'}, inplace=True)
        df_lst.append(df)
    df = pd.concat([d for d in df_lst])
    df['DATECODE'] = df['DATECODE'].astype(str)
    save_iter(df, ITER)


def iter_checking(ITER_IN:str, ITER:str, time_resol:str = 'DATECODE', space_resol:str = '3AGY'):
    df = pd.read_pickle(f'{ITER_IN}.pkl')
    #df.reset_index(inplace=True)
    df = df.rename(columns={df.index.name:'index'})
    if ITER == 'checking_out':
        # filter out 10% of bottom agencies, less than 10 rows, (some < 3 years)
        df = branching(df,time_resol, space_resol, branch='senate', from_top=False)
        

    elif ITER == 'checking_in':
        df = branching(df, time_resol, space_resol, branch='senate', from_top=False)
    
    save_iter(df, ITER)


def iter_forming(ITER_IN:str, ITER:str, disagg: str, time_resol:str= 'DATECODE', space_resol:str = '3AGY'): # ratio total 
    '''
    ITER_IN: checking_out, checking_out
    ITER: forming_share_size, forming_cluster. chained (ITER_IN, ITER) makes dict() input a better implementation, by (checking_out, forming_cluster) may be possible
    diagg: by_s, by_st, by_t
    time_resol: 'month', 'year' can be derived from 'DATECODE' #TODO
    '''
    df = pd.read_pickle(f'{ITER_IN}.pkl')
    if ITER == 'forming_size_share':
        # for clustering, it might help to have further specification
        # space_resol = '3AGY':
            # clustering happens on the same level of one agent
        # space_resol =  '4AGYSUB'
            # clustering happens on the one level up of one agent (agency)

        if disagg == 'by_s':
            ts_group = df.groupby(space_resol)

        elif disagg == 'by_t':
            ts_group = df.groupby(time_resol)

        elif disagg == 'by_ts':
            ts_group = df.groupby([space_resol, time_resol])

        s_size = ts_group['EMPLOYMENT'].sum()
        mng = ts_group['5is_mng'].sum()
        mng_frac = pd.concat([s_size, mng], axis =1, ignore_index=False) #indexing with space_resol
        mng_frac.rename(columns={"EMPLOYMENT":"s_size"}, inplace = True)
        mng_frac["reg_frac"]= mng_frac["5is_mng"]/mng_frac["s_size"]
        mng_frac.reset_index(inplace=True)
        save_iter(mng_frac, ITER, disagg) #if merge takes too long
        
    elif ITER == 'forming_cluster':
        df = pd.read_pickle(f'{ITER_IN}.pkl')
        max_comp = 4
        cf = np.zeros(max_comp).tolist()
        def standardize(df:pd.Series) -> pd.Series:
            return (df-df.median())/(df.max() - df.min())
        def log_standardize(df:pd.Series) -> pd.Series:
            df = df.apply(np.log)
            return (df-df.median())/(df.max() - df.min())

        cluster_df = df.assign(std_size = log_standardize(df.s_size), std_ratio = standardize(df.reg_frac)).groupby(space_resol).mean()
        cluster_df.dropna(inplace = True) #3 dropped from log(ratio =0)
        for m in range(2, max_comp):
            cf[m] = GaussianMixture(n_components = m).fit(X = cluster_df[['std_size', 'std_ratio']])
            cluster_df.loc[:, f'c_{m}'] = cf[m].predict(X = cluster_df[['std_size', 'std_ratio']])
            scale_plot(df, disagg, time_resol, space_resol)
            plt.figure(figsize=(15,8))
            sns.scatterplot(cluster_df,  x='std_size', y='std_ratio', hue= f'c_{m}')
            plt.savefig(f"{get_plot_path('agency')}/c_{m}_cluster_{disagg}" + ".png")
        #clustered = df.merge(cluster_df, on = space_resol,)
        save_iter(cluster_df, ITER, disagg)

def iter_plotting(ITER_IN, ITER, disagg):
    # EB vs HF, Education large variation
    df = pd.read_pickle(f'{ITER_IN}.pkl')

    scale_plot(df, disagg)

    save_iter(df, ITER, disagg)


def branching(df, time_resol:str= 'DATECODE', space_resol:str = '3AGY',branch='senate', from_top=True):
    """
    features: features from below to be tracked other than agnecy hierarchy five level ('AGYTYP', 'AGY', 'AGYSUB') e.g. SALARY
    # original data FACDATA.txt col" ['AGYSUB', 'LOC', 'AGELVL', 'EDLVL', 'GSEGRD', 'LOSLVL', 'OCC', 'PATCO',
    #          'PP', 'PPGRD', 'SALLVL', 'STEMOCC', 'SUPERVIS', 'TOA', 'WORKSCH',
    #          'WORKSTAT', 'DATECODE', 'EMPLOYMENT', 'SALARY', 'LOS', 'AGYTYP',
    #          'AGYTYPT', 'AGY', 'AGYT', 'AGYSUBT'] and by default it is organized into 1-4-130-530-1060 hierarchy
    
    layers: degree of fineness for organization hierarchy after merge(fact,agy)-> groupby, it hierarchize according to `layers`.
    layer 5:                     SUPERVIS
    layer 4:                AGYSUB
    layer 3:              AGY
    layer 2:        AGYTYP
    layer 1: AGY_arch
    """
    if branch == 'mng':
        df['is_mng'] = df["SUPERVIS"].isin(['2', '6', '7']) 

    elif branch == 'senate': # us federal agency, by agency
        #df = df.reset_index()
        size = len(set(df[space_resol]))
        if 'EMPLOYMENT' in df.columns:
            sorted_state = df.groupby(space_resol)['EMPLOYMENT'].count().sort_values()
        else:
            sorted_state = df.groupby(space_resol)['s_size'].count().sort_values()
        # VA: dep. verterans affairs (defense) 300k - why this many? + some innovative dep??
        # AR: dep. of army (defense) 250k
        # NV: dep. of navy (defense) 200k
        # AF: dep. of air force (defense) 150k
        # HS: dep. homeland security (defense) 100k
        # DJ: dep. justice 100k
        # TR: dep. treasury 100k
        # DD: dep. of defense 100k
        # AG: dep. of agriculture 100k (innovative)
        # HE: dep. of health and human service 75k
        if from_top:
            for tq in [.02, .05, .1]:
                s_state = sorted_state[int(-size*tq):]
                df = df.iloc[(np.where(~df[space_resol].isin(s_state.index)))]  
                #df = df.assign(is_stop = lambda x: x[space_resol].isin(s_state)) #doesn't filter out
                df.rename(columns = {'is_stop': f'is_stop{tq}'}, inplace=True)
        else:
            for bq in [.1]:
                s_state = sorted_state[:int(size*bq)]
                df = df.iloc[(np.where(~df[space_resol].isin(s_state.index)))] # cut-off 200, 'DO', 'GN', 'YG', 'DA', 'EV', 'IP', 'ZQ', 'ZN', 'YA', 'GU', 'WK', 'GZ','ZK', 'KY', 'AC', 
                #'YE' (two years) COMMISSION ON THE PREVENTION OF WEAPONS OF MASS DESTRUCTION PROLIFERATION AND TERRORISM
                df.rename(columns = {'is_sbot': f'is_sbot{bq}'}, inplace=True)
            #similar effect with df  = df[~(df.s_size < 10)] EXCEPT no s_size yet so need to extract index by first groupby 

    elif branch == 'representative': # us federal agency as a whole, proportional
        size = df.shape[0]
        sorted_state_cumsum = df.groupby(space_resol)['s_size'].count().sort_values().cumsum()
        if from_top:
            for tq in [.02, .05, .1]:
                r_state = sorted_state_cumsum > size* (1-tq)
                df[f'is_rtop{tq}'] = df[(np.where(~df[space_resol].isin(s_state.index)))] # doesn't work #TODO
                df = df.assign(is_rtop = lambda x: x[space_resol].isin(r_state))
                df.rename(columns = {'is_rtop': f'is_rtop{tq}'}, inplace=True)    
        else:
            for bq in [.1]:
                r_state = sorted_state_cumsum < size* bq
                df = df.assign(is_rbot = lambda x: x[space_resol].isin(r_state))
                df.rename(columns = {'is_rbot': f'is_rbot{bq}'}, inplace=True)
    return df

def scale_plot(df, disagg, time_resol = 'DATECODE', space_resol = '3AGY'):
    space_resol_angle = dict(
        top1=['VA', 'AR'],
        top5=['VA', 'AR', 'NV','AF','HS'],
        top10=['VA', 'AR', 'NV','AF','HS','DJ','TR','DD','AG','HE'],
        defense=['AR','NV', 'AF','HS', 'DD'],
        responsive=['NN']
    )
    plot_path = get_plot_path('agency')
    figsize = (20, 20)
    if disagg == "by_t": # TODO meaning of scaling analysis with marginalize over agency, one agency's time series is tricky for scaling analysis
        fig, axes = plt.subplots(1,2, figsize = figsize)
        # need groupby(space_resol), but seaborn provides "Passing the entire dataset in long-form mode will aggregate over repeated values (each year) to show the mean and 95% confidence interval:"
        axes[0].tick_params(axis='x', rotation=45)
        axes[1].tick_params(axis='x', rotation=45)
        sns.lineplot(df, x='DATECODE', y='reg_frac', ax = axes[0]) # disagg by time = groupby space!
        sns.lineplot(df, x='DATECODE', y='s_size', ax = axes[1]) 

    elif disagg == "by_s": # space disaggregation
        _, axes = plt.subplots(1, len(space_resol_angle), figsize=figsize)
        plt.setp(axes, xlim = (10**5,5*10**6), ylim = (0,100))
        for i, agg in enumerate(space_resol_angle.values()): 
            axes[i].set(xscale="log", yscale="log")
            sns.scatterplot(df[df[space_resol].isin(agg)],  x='s_size', y='reg_frac',hue=space_resol, ax = axes[i])
        
    elif disagg == "by_ts": # timeXspace disaggregation
        _, axes = plt.subplots(1, len(space_resol_angle), figsize=figsize)
        for i, agg in enumerate(space_resol_angle.values()):
            axes[i].set(xscale="log", yscale="log")
            sns.scatterplot(df[['s_size', 'reg_frac',time_resol]],  x='s_size', y='reg_frac',hue=time_resol, ax = axes[i])
    plt.show()
    plt.savefig(f"{get_plot_path('agency')}/loglog_share_size_{disagg}" + ".png")
    plt.clf()
