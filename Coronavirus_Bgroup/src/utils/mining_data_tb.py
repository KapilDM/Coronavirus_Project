import pandas as pd

def changing_dates(df, name_column): 
    """changing the date type to datatime"""
    df[name_column] = df[name_column].astype('datetime64[ns]')