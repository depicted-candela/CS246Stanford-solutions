import math
import matplotlib.pyplot as plt
import pandas as pd

def tt(s, t, h, p, c):
    ## time without fails
    tnf = s * t
    ## possible fails given steps
    f = s * p
    ## time per fail
    tf = f * h * t
    ## time for checkpoints
    th = s / h * c * t
    ## total time
    tt = tnf + tf + th
    return tt

def h(c, p):
    return abs(math.sqrt(c / p))

s = 100
t = 1
p = 0.01
c = 2*t

dic = {"steps": [], "time": [], "ht": [], "hi": [], "p": [], "c": [], "tt": []}

for k in range(1, 5, 1):
    for j in range(100, 1000, 200):
        for i in range(1, int(h(c, p)) * 5):
            dic["steps"].append(j)
            dic["time"].append(t)
            dic["ht"].append(h(c, k / 100))
            dic["p"].append(k / 100)
            dic["c"].append(c)
            dic["hi"].append(i)
            dic["tt"].append(tt(j, t, i, k / 100, c))

df = pd.DataFrame(dic)

plt.figure(figsize=(8, 6))  # Optional: Set the figure size

# Loop through unique categories and create scatter plots for each category
for (cat1, cat2), group in df.groupby(['steps', 'p']):
    plt.plot(group['hi'], group['tt'], label=f'{cat1}, {cat2}')
    # plt.plot(group['ht'].iloc[0],
    #          tt(group["steps"].iloc[0], t, group["ht"].iloc[0], p, c),
    #          marker='o',
    #          color='red')
    plt.plot(group[group['tt'] == min(group['tt'])]['hi'].iloc[0],
            group[group['tt'] == min(group['tt'])]['tt'].iloc[0],
            marker='X',
            color='black')
    print(group[group['tt'] == min(group['tt'])][['ht', 'tt', 'p', 'steps']])
    plt.plot(group[group['tt'] == min(group['tt'])]['ht'].iloc[0],
            group[group['tt'] == min(group['tt'])]['tt'].iloc[0],
            marker='o',
            color='red')

# Add labels and legend
plt.xlabel('hi')
plt.ylabel('tt')
plt.title('Scatter Plot Categorized by SuperSteps Variable')
plt.legend(title='Category')

# Show the plot
plt.grid(True)
plt.show()