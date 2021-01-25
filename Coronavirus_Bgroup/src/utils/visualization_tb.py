import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys
import pandas as pd

root_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(root_path)

def cm_to_inch(value):
    """Changing the size of the graphs from cm to ich"""
    return value/2.54


def funcion_para_añadir_una_barra(string):
    """Adding the double bar to the path"""
    result = string.replace("\\", r"\\")
    print(result)
    return result

def get_row_countries(df, row, countr_list):
    '''
        Returns list of lists with names of countries and tuples for that country's row values and date values
    '''
    lis = []
    for el in countr_list:
        l = [el]
        l.append(tuple(df[(df["location"] == el)][row]))
        l.append(tuple(df[(df["location"] == el)].date))
        lis.append(l)

    return lis

def plot_row_countries(axes_list):
    '''
        Plots line graphs for every list of axes_list list of lists
    '''
    sns.set()
    
    colour = ['r', 'y', 'g', 'b', '#6B737E']
    plt.figure(figsize=(cm_to_inch(30),cm_to_inch(15)))
    for i, axes in enumerate(axes_list):
        plt.plot(axes[2], axes[1], color=colour[i], linewidth= 3, label=axes[0])

def prcnt_plt(df):
    '''
        Relative value plot
    '''
    sns.set()
    plt.figure(figsize=(cm_to_inch(30), cm_to_inch(15)))

    for col in df:
        x_axes = df[col].index
        y_axes = df[col].values
        plt.plot(x_axes, y_axes, linewidth= 3)

    plt.legend(df.columns)

def plot_def(df, row, countr_list, ylab=None, title=None):
    axes_list = get_row_countries(df=df, row=row, countr_list=countr_list)
    plot_row_countries(axes_list= axes_list)
    if ylab:
        ylab = ylab
    else:
        ylab = row
    label_fig(title=title, xlab='Date', ylab=ylab)
    plt.xticks(rotation="90")
    plt.legend()

def country_alarm_state_func(df,country):
    #@KapilDM
    y_total_cases = df[(df["location"] == country)].total_cases
    y_total_cases_per_million = df[(df["location"] == country)].total_cases_per_million
    y_new_cases_smoothed = df[(df["location"] == country)].new_cases_smoothed
    y_new_cases_smoothed_per_million = df[(df["location"] == country)].new_cases_smoothed_per_million
    y_new_deaths_smoothed = df[(df["location"] == country)].new_deaths_smoothed
    y_new_deaths_smoothed_per_million = df[(df["location"] == country)].new_deaths_smoothed_per_million
    y_total_deaths = df[(df["location"] == country)].total_deaths
    y_total_deaths_per_million = df[(df["location"] == country)].total_deaths_per_million
    y_stringency_index = df[(df["location"] == country)].stringency_index
    y_life_expectancy = df[(df["location"] == country)].life_expectancy
    y_new_deaths = df[(df["location"] == country)].new_deaths

    lista = [y_total_cases,y_total_cases_per_million,y_new_cases_smoothed,y_new_cases_smoothed_per_million,
    y_new_deaths_smoothed,y_new_deaths_smoothed_per_million,y_total_deaths,y_total_deaths_per_million,  
    y_stringency_index,y_life_expectancy,y_new_deaths]
    lista2 = ["Total_cases","Total cases per million","New cases smoothed", "New cases smoothed per million","New deaths smoothed",
    "New deaths smoothed per million","Total deaths","Total deaths per million","Stringency index",
    "Life expectancy","New deaths"]

    #sns.set_style("whitegrid")
    x_plot = df[(df["location"] == country)].date
    for pos,val in enumerate(lista):
        sns.set()
        plt.figure(figsize=(cm_to_inch(30),cm_to_inch(15)))
        plt.title(str(country) + " - " + lista2[pos], fontdict={"fontsize":15, "fontweight":"bold"} ) #HE cambiado esto 
        plt.xlabel("Date", weight="bold")
        plt.ylabel(lista2[pos], weight="bold")
        plt.xticks(rotation="90")

        if lista2[pos] == "Stringency index":
            plt.ylim([0,100])

        if country == "France":
            plt.plot(x_plot.values, val, color='r', label = lista2[pos],linewidth= 2)
            plt.axvline(pd.to_datetime('2020-03-23'), color="#9433FF", linestyle='--', lw=2, label='FIRST: Start /End alarm state')
            plt.axvline(pd.to_datetime('2020-07-10'), color="#9433FF", linestyle='--', lw=2)
            plt.axvline(pd.to_datetime('2020-10-17'), color="#F633FF", linestyle='--', lw=2, label='SECOND: Start alarm state')
            plt.axvspan(pd.to_datetime('2020-03-23'), pd.to_datetime('2020-07-10'), alpha=0.04, color='#9433FF')
            plt.savefig(root_path + "\\reports\\France\\" + lista2[pos] + ".png", dpi=300, bbox_inches='tight')
        elif country == "Spain":
            plt.plot(x_plot.values, val, color='y', label = lista2[pos],linewidth= 2)
            plt.axvline(pd.to_datetime('2020-03-14'), color="#9433FF", linestyle='--', lw=2, label='FIRST: Start /End alarm state')
            plt.axvline(pd.to_datetime('2020-06-21'), color="#9433FF", linestyle='--', lw=2)
            plt.axvline(pd.to_datetime('2020-10-25'), color="#F633FF", linestyle='--', lw=2, label='SECOND: Start alarm State')
            plt.axvspan(pd.to_datetime('2020-03-14'), pd.to_datetime('2020-06-21'), alpha=0.04, color='#9433FF')
            plt.savefig(root_path + "\\reports\\Spain\\" + lista2[pos] + ".png", dpi=300, bbox_inches='tight')
        elif country == "India":
            plt.plot(x_plot.values, val, color='g', label = lista2[pos],linewidth= 2)
            plt.axvline(pd.to_datetime('2020-03-24'), color="#9433FF", linestyle='--', lw=2, label='FIRST: Start /End alarm state')
            plt.axvline(pd.to_datetime('2020-05-31'), color="#9433FF", linestyle='--', lw=2)
            plt.axvspan(pd.to_datetime('2020-03-24'), pd.to_datetime('2020-05-31'), alpha=0.04, color='#9433FF')
            plt.savefig(root_path + "\\reports\\India\\" + lista2[pos] + ".png", dpi=300, bbox_inches='tight')
        elif country == "Peru":
            plt.plot(x_plot.values, val, color='b', label = lista2[pos],linewidth= 2)
            plt.axvline(pd.to_datetime('2020-03-15'), color="#9433FF", linestyle='--', lw=2, label='FIRST: Start alarm state')
            plt.savefig(root_path + "\\reports\\Peru\\" + lista2[pos] + ".png", dpi=300, bbox_inches='tight')
        elif country == "United States":
            plt.plot(x_plot.values, val, color='#6B737E', label = lista2[pos],linewidth= 2)
            plt.axvline(pd.to_datetime('2020-03-15'), color="#9433FF", linestyle='--', lw=2, label='FIRST: Start Alarm State')
            plt.savefig(root_path + "\\reports\\United_States\\" + lista2[pos] + ".png", dpi=300, bbox_inches='tight')
            
        plt.legend()
        plt.show()

def prcnt_df(df, column):
    cases_percnt = pd.DataFrame()
    for col in df.columns[:-1]:
        cases_percnt[col] = (df[col]/df[column])*100
    return cases_percnt

def prcnt_plt(df):
    plt.figure(figsize=(cm_to_inch(30), cm_to_inch(15)))
    colour = ['r', 'g', 'b', 'y', '#6B737E']

    for i,col in enumerate(df):
        x_axes = df[col].index
        y_axes = df[col].values
        plt.plot(x_axes, y_axes, linewidth= 3, color=colour[i])

    plt.legend(df.columns)

####### Labelling and saving functions

def label_fig(title=None, xlab=None, ylab=None, tit_size=15):
    if title:
        plt.title(title, fontsize=tit_size)
    if xlab:
        plt.xlabel(xlab, weight="bold")
    if ylab:
        plt.ylabel(ylab, weight="bold")

def save_resources(name):
    root_project = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    plt.savefig(root_project + f'//reports//{name}.png', dpi=300, bbox_inches='tight')