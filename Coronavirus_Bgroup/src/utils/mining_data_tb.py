import pandas as pd
import json

def changing_dates(df, name_column): 
    """changing the date type to datatime"""
    df[name_column] = df[name_column].astype('datetime64[ns]')

def country_select(df, count_list):
    '''
        Returns filtered dataframe with countries in count_list
    '''
    count_df = pd.DataFrame()
    for country in count_list:
        step_df = df[df["location"] == country]
        count_df = count_df.append(step_df)
    
    return count_df

def grouped_df(df, group_col, select_col=None, col_name=None):
    '''
        Returns grouped column. If select_col, the return will be a dataframe with that one column.
        If col_name, new column with that name
    '''
    out_df = df.groupby(f"{group_col}").mean()
    if select_col:
        out_df = out_df[f'{select_col}'].to_frame()
        if col_name:
            out_df.columns=[f'{col_name}']

    return out_df

def null_clean(df):
    return df.dropna()

def df_to_json(df):
    '''
        Gets dataframe, returns json 
    '''
    return df.to_json(orient="columns")

def n_d_averages_json():
    '''
        Returns an updated new of death averages json from the covid dataframe
    '''
    covid_df = pd.read_csv("https://covid.ourworldindata.org/data/owid-covid-data.csv")
    covid_df = country_select(df=covid_df, count_list=['India', 'Peru', 'United States', 'France', 'Spain'])
    changing_dates(df=covid_df,name_column="date") 
    covid_df = grouped_df(df=covid_df, group_col='date', select_col='new_deaths', col_name='n_d_averages')
    covid_df = null_clean(covid_df)
    covid_json = df_to_json(covid_df)

    return json.loads(covid_json) 
