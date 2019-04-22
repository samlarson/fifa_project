# THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING
# A TUTOR OR CODE WRITTEN BY OTHER STUDENTS - Shayan Jiwani, Sam Larson, Safa Tinaztepe


import warnings
import pandas as pd


# Suppress a Pandas warning for setting dataframe columns from a copy slice
warnings.filterwarnings('ignore', 'SettingWithCopyWarning')
pd.set_option('mode.chained_assignment', None)


# Loads data from an Excel (.csv) file, and cleans the specified columns
# Opens Pandas dataframe and calls function to fill blank values
def load_data(data_path):
    load = pd.read_csv(data_path, sep=",")
    df = preproc_euros(fill_missing(load))
    return df


# Fill missing matrix cells with 0's to allow column computations
def fill_missing(to_clean):
    for col in to_clean.columns:
        to_clean[col].fillna(0, inplace=True)
    return to_clean


# Remove string components from currency-related columns, converts columns to float64 true-values
def preproc_euros(df):
    check_cols = df.columns
    currency_cols = ['Value', 'Wage', 'Release Clause']
    df[check_cols] = df[check_cols].replace({'\€': ''}, regex=True)
    df[currency_cols] = df[currency_cols].apply(lambda x: x.str.strip('KM'))

    df[currency_cols] = df[currency_cols].apply(pd.to_numeric, errors='coerce')
    df['Value'] = df['Value'].mul(1000000, axis=0)
    df['Release Clause'] = df['Release Clause'].mul(1000000, axis=0)
    df['Wage'] = df['Wage'].mul(1000, axis=0)

    return df


def score_regex(df):
    for col in df.iloc[:, 28:54]:
        for cell in df[col]:
            if cell == 0 or cell == '':
                continue
            elif '+' not in str(cell):
                continue
            else:
                score = str(cell)
                score_one, score_two = score.split('+')
                df.loc[cell, col] = float(score_one) + float(score_two)
                # print(df.loc[cell, col])

    return df


# Print a dataframe displaying all cell values
def df_print(df):
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(df)


data_path = 'data/ex_fifa.csv'
fifa_df = load_data(data_path=data_path)

# keep = ['Name', 'Value', 'Wage', 'Release Clause']
# fifa_df = fifa_df[keep]

score_regex(fifa_df)


# TODO: convert categorical variables/one-hot encode
# drop_cols = ['Photo', 'Flag', 'Club Logo', 'Real Face', ]
# df.drop(columns=drop_cols)

