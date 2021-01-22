import pandas as pd
from src.utils.mining_data_tb import *

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