
#TODO start from joining two dataframes 11.W2
def movie_compare(old_df, new_df):
    print(old_df.title)
    print(new_df.title)
    print(len(old_df.title))
    print(len(new_df.title))
    on_title = pd.merge(old_df, new_df, on = "title")
    print(len(new_df.title))
    print(on_title.title)
    return


def print_shape(old, new):
    return old.shape[0], new.shape[0]


def multi_col_unique(df):
    test = df.assign(
        old_id =df.index.to_series().groupby(
            [df.title, df.year]
        ).transform('first').map('OLD{}'.format)
    )[['old_id'] + df.columns.tolist()]
    return test
