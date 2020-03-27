import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import operator

data = pd.read_csv("ascents.csv")
climbers= data["Name"]

climberCounts = dict()
for climber in climbers:
    if climber in climberCounts:
        climberCounts[climber] = climberCounts[climber] + 1
    else:
        climberCounts[climber] = 1

#sort items
sorted_climber_counts = sorted(climberCounts.items(), key=operator.itemgetter(1))
print(sorted_climber_counts)

climbers = []
ascents = []
for climber,count in sorted_climber_counts:
    climbers.append(climber)
    ascents.append(int(count))

y_pos = np.arange(len(climbers))

plt.bar(y_pos, ascents, align='center', alpha=0.5)
plt.xticks(y_pos,climbers, rotation="vertical")
plt.ylabel('V13 ascents (or harder)')
plt.title('Female Boulders by Ascents')
plt.tight_layout()
plt.savefig("climbers.pdf")




"""
plt.plot(x,y, label='Loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
"""
