import argparse
import pandas as pd
import json

class Comando:

    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-j", "--j", type=int, help="the password, for correct answer insert 18", required=True)
        self.args = vars(parser.parse_args())

    def json_df(self):
        data = pd.read_csv("https://covid.ourworldindata.org/data/owid-covid-data.csv")
        data_sc = data[(data["location"] == "India") | (data["location"] == "Peru") | (data["location"] == "United States") | (data["location"] == "France") | (data["location"] == "Spain")]
        
        data_sc["date"] = data_sc["date"].astype('datetime64[ns]')
        
        df_api = data_sc.groupby(["date"]).mean()["new_deaths"].to_frame()
        df_api.columns = ["n_d_averages"]
        
        result = df_api.to_json(orient="columns")
        parsed = json.loads(result)
        
        base = self.args["j"]

        return print("\n######################\nThis is the json of B Group\n######################\n\n", parsed) if base == 18 else print("\n######################\nSorry, this is not the correct answer\n######################\n\n")

comando_18 = Comando()
comando_18.json_df()

# TO RUN: 
#python C:\Users\maria\OneDrive\Escritorio\The_Bridge\Visual_Studio_Code\Python\EDA_projects\Coronavirus_Bgroup\src\services\argparse\console.py -j 18

# 1
# python o python3 
# 2
# ruta al fichero 
# 3
# args
# --help

# 'python' 'ruta' 'args'