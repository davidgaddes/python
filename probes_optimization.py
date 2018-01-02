'''Determines a sequence to create probes using the greedy algorithum'''
import collections as col
import pandas as pd
import numpy as np

df = pd.read_csv('Probes.csv')
df['Probe Length'] = df['Probes'].apply(lambda s: len(s))

for word in list(df['Probes']):
    print(word)
cnt = col.Counter()
step = []
expedite = []
process = True

while process is True:
    for word in list(df['Probes']):
        step.append(word[cnt[word]])
    nucleotide = np.array(col.Counter(step).most_common(1))
    expedite.append(nucleotide[0, 0])
    for word in list(df['Probes']):
        if word[cnt[word]] == nucleotide[0, 0]:
            cnt[word] += 1
        if cnt[word] == len(word):
            process = False
print(expedite)
print(len(expedite))


