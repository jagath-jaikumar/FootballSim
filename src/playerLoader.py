import pandas as pd
import json
from lib.player import Player  


def read_data(fromPickle = False):
    pickleName = "data/py_objects/M20_players.pkl"
    if not fromPickle:
        datapath = "data/raw/M20_players.csv"
        players_df = pd.read_csv(datapath)
        players_df.to_pickle(pickleName)
    else:
        players_df = pd.read_pickle(pickleName)

    return players_df

def main():
    players_df = read_data(fromPickle = True)
    players_df = players_df.drop(['Unnamed: 69','primary key', 'encrypted id'], axis=1)
    stat_names = list(players_df.columns)
    players = []
    for k, row in players_df.iterrows():
        p_dic = {}
        for i in stat_names:
            p_dic[i] = row[i]
        p = Player(p_dic)
        players.append(p)

    with open('data/py_objects/M20_players.json', 'w') as f:
        for p in players:
            json.dump(p.stats, f, indent=4, separators=(',', ': '))


if __name__ == "__main__":
    main()