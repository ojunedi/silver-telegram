from itertools import combinations
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
import csv
import os


stats = pd.read_csv("C:/Data Analysis/Clash Royale/Clash_Stats.csv")  # clash royale stats from royaleapi.com



def get_rows():
    path = r"C:/Data Analysis/Clash Royale/Clash_Stats.csv"
    assert os.path.isfile(path)
    with open(path, "r", encoding="UTF-8") as f:
        csv.reader(f)
        value = len(list(f))
        return value - 1


# List of games lost
losses = [j for j in range(get_rows()) if stats["team_0_crowns"][j] < stats["opponent_0_crowns"][j]]



# Putting decks into lists 
decks = []
for i in losses:
    my_deck = [stats["team_0_cards_0_name"][i], stats["team_0_cards_1_name"][i],
               stats["team_0_cards_2_name"][i], stats["team_0_cards_3_name"][i],
               stats["team_0_cards_4_name"][i], stats["team_0_cards_5_name"][i],
               stats["team_0_cards_6_name"][i], stats["team_0_cards_7_name"][i]]

    opp_deck = [stats["opponent_0_cards_0_name"][i], stats["opponent_0_cards_1_name"][i],
                stats["opponent_0_cards_2_name"][i], stats["opponent_0_cards_3_name"][i],
                stats["opponent_0_cards_4_name"][i], stats["opponent_0_cards_5_name"][i], 
                stats["opponent_0_cards_6_name"][i], stats["opponent_0_cards_7_name"][i]]
    decks.append(opp_deck)




# Counting cards in decks
counter = Counter(decks[0])
for i in decks:
    counter.update(i)
counter.most_common()






# Plotting single card freq
plt.style.use('seaborn')
data = counter.most_common()
name = [name[0] for name in data[:16]]
freq = [name[1] for name in data[:16]]
plt.figure(figsize=(18, 5))
plt.bar(name, freq, align='center', width=0.5, color='#87CEEB')
plt.xticks(fontsize=8)
plt.show()




# Dictionary counter of card combos
combo_wombo = {}
for deck in decks:
    sub_combos = list(combinations(deck, 2))
    for i in sub_combos:
        if i in combo_wombo:
            combo_wombo[i] = 1 + int(combo_wombo.get(i))
        else:
            combo_wombo[i] = 0




# Converting dictionary into two lists for plotting
names = []
values = []
for pair in combo_wombo.items():
    if pair[1] > 0:
        values.append(pair[1]+1)
        names.append(pair[0])
for i in range(len(names)):
    names[i] = f'''{names[i][0]}
{names[i][1]}'''



# Plotting Card Combos Freq
plt.style.use('seaborn')
plt.figure(figsize=(18, 5))
plt.bar(tuple(names), tuple(values), align='center', width=0.5, color='#87CEEB')
plt.xticks(fontsize=7)
plt.show()
