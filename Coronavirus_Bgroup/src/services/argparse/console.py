import argparse
import pandas as pd
import json
import os
import sys

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(root_path)


from src.utils.folders_tb import open_json
from src.utils.apis_tb import n_d_averages_json

class Comando:

    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-j", "--j", type=int, help="the password, for correct answer insert 18", required=True)
        self.args = vars(parser.parse_args())

    def json_df(self):
        
        base = self.args["j"]

        return print("\n######################\nThis is the json of B Group\n######################\n\n", n_d_averages_json()) if base == 18 else print("\n######################\nSorry, this is not the correct answer\n######################\n\n")

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