
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

def match_movie_info():
    """
    given old and new dataframe with movie_title, year, old_id (old) and movie_title, year, new_id (new),
    returns 1. unified union dataframe with movie_title, union_id, year
            2. map of (old_id, union_id), (new_id, union_id)
    """
    # TODO need to add old_id for old_movie
    return



def match_person_info():
    """
    given old and new dataframe with person name, old_id (old) and person name, birthyear, new_id (new),
    returns 1. unified union dataframe with person name, id, person name, birthyear
            2. map of (old_id, union_id), (new_id, union_id)
    """
    return