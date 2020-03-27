import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import operator

data = pd.read_csv("ascents.csv")
boulders= data["Boulder"]

boulderCounts = dict()
for boulder in boulders:
    if boulder in boulderCounts:
        boulderCounts[boulder] = boulderCounts[boulder] + 1
    else:
        boulderCounts[boulder] = 1

tmp = dict()
for boulder in boulderCounts:
    if boulderCounts[boulder] > 1:
        tmp[boulder] = boulderCounts[boulder]
boulderCounts=tmp

#sort items
sorted_boulder_counts = sorted(boulderCounts.items(), key=operator.itemgetter(1))

boulders = []
ascents = []
for boulder,count in sorted_boulder_counts:
    boulders.append(boulder)
    ascents.append(int(count))

y_pos = np.arange(len(boulderCounts))

plt.bar(y_pos, ascents, align='center', alpha=0.5)
plt.xticks(y_pos,boulders, rotation="vertical")
plt.ylabel('Ascents')
plt.xlabel('V13 or harder with more than 1 ascent')
plt.title('Female Boulders by Ascents')
plt.tight_layout()
plt.savefig("boulders.pdf")