from lib.player import Player
from lib.team import Team 
from lib.football import FootballGame
from src.generateTeam import getTeam

import matplotlib.pyplot as plt
import pandas as pd

def getRPR(teams):
    rpr = []
    for team in teams:
        t = getTeam(team = team, verbose = False)
        rpr.append(t.run_pass_ratio)
    return rpr


def plot(x, y, name):
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = 'Helvetica'

    plt.rcParams['axes.edgecolor']='#333F4B'
    plt.rcParams['axes.linewidth']=0.8
    plt.rcParams['xtick.color']='#333F4B'
    plt.rcParams['ytick.color']='#333F4B'
    plt.rcParams['text.color']='#333F4B'

    data = pd.Series(y,index=x)

    df = pd.DataFrame({name : data})
    df = df.sort_values(by=name)

    my_range=list(range(1,len(df.index)+1))
    fig, ax = plt.subplots(figsize=(5,10))
    plt.hlines(y=my_range, xmin=.9, xmax=df[name], color='#007ACC', alpha=0.2, linewidth=5)

    plt.plot(df[name], my_range, "o", markersize=5, color='#007ACC', alpha=0.6)

    ax.set_xlabel(name, fontsize=15, fontweight='black', color = '#333F4B')
    ax.set_ylabel('')

    ax.tick_params(axis='both', which='major', labelsize=12)
    plt.yticks(my_range, df.index)

    fig.text(0, .9, name, fontsize=18, fontweight='black', color = '#333F4B')
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_smart_bounds(True)
    ax.spines['bottom'].set_smart_bounds(True)
    ax.spines['bottom'].set_position(('axes', -0.04))
    ax.spines['left'].set_position(('axes', 0.015))

    filename = 'visualization/' +name + '.png'
    plt.savefig(filename, dpi=300, bbox_inches='tight')

def main():
    teams = ['ari','atl','bal','buf','car','chi','cin','cle','dal', 'den', 'det', 'gb', 'hou', 'ind','jax','kc', 'lac', 'lar', 'lv','mia','min','ne','no','nyg','nyj','phi','pit','sea','sf','tb','ten','was']
    rpr = getRPR(teams)
    plot(teams,rpr, 'RunPassRatio')




if __name__ == "__main__":
    main()