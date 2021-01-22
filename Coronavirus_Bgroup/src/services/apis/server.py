from flask import Flask,request,jsonify
import json
import os, sys
import pandas as pd

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(root_path)


from src.utils.folders_tb import open_json
from src.utils.apis_tb import n_d_averages_json

app = Flask(__name__)

@app.route("/")
def home():
    return "Hola, bienvenido a la API"

@app.route("/group_id", methods=['GET'])
def group_id():                          
    N = "B88"                            
    contrasenia = request.args["password"]                                
    if contrasenia == N:                 
        return jsonify({"token" : "B227766764"})
    else:
        return "group_id is incorrect, please introduce B88 ;)"


@app.route("/token_id", methods=['GET']) #Habria que poner despues de /token_id?password=B227766764
def token_id():
    S = "B227766764"
    contrasenia = request.args["password"] 
    if (contrasenia == S):
        json_b_group = n_d_averages_json()
        return json_b_group #open_json(path_json) 
    else:
        return "CONTRASEÑA INCORRECTA"



if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=6060) 
 
    