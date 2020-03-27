import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import operator




color_v13=sns.xkcd_rgb["medium blue"]
color_v14=sns.xkcd_rgb["medium green"]
color_v15=sns.xkcd_rgb["tomato red"]

data = pd.read_csv("ascents.csv")
difficulty=data["V Grade"]
year=data["Year"]

print(len(year))
print(len(difficulty))



v13 = dict()
v14 = dict()
v15 = dict()

for v, y in zip(difficulty,year):
    y2 = int(y)
    if v == "V13":
        if y2 in v13:
            v13[y2] = v13[y2] + 1
        else:
            v13[y2] =1 
    elif v == "V14":
        if y2 in v14:
            v14[y2] = v14[y2] + 1
        else:
            v14[y2] =1 
    elif v == "V15":
        if y2 in v15:
            v15[y2] = v15[y2] + 1
        else:
            v15[y2] =1 

#add 0's for prettier lines
for y in v13:
    if not y in v14:
        v14[y] = 0
    if not y in v15:
        v15[y] = 0



year_13 = []
climbs_13 = []
for y in sorted(v13):
    year_13.append(int(y))
    climbs_13.append(int(v13[y]))

year_14 = []
climbs_14 = []
for y in sorted(v14):
    year_14.append(int(y))
    climbs_14.append(int(v14[y]))

year_15 = []
climbs_15 = []
for y in sorted(v15):
    year_15.append(int(y))
    climbs_15.append(int(v15[y]))



width=3
plt.plot(year_13,climbs_13,linewidth=width,marker="o",label="V13",color=color_v13)
plt.plot(year_14,climbs_14,linewidth=width,marker="x",label="V14",color=color_v14)
plt.plot(year_15,climbs_15,linewidth=width,marker="*",label="V15",color=color_v15)
plt.legend()
plt.ylabel('Ascents Per Year')
plt.title('Female Boulder Ascents over time')
plt.tight_layout()
plt.savefig("difficulty_year.pdf")