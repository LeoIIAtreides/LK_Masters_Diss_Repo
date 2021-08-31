import pandas as pd

vaderAvg = pd.read_excel("VADER ID+AVG.xlsx")
vaderAvg = vaderAvg[vaderAvg["Avg_Comp"].notna()]
vaderAvg.to_csv("Vader_Avg_Pruned.csv", index=True, encoding='utf8')

liwcAvg = pd.read_excel("LIWC ID+AVG.xlsx")
liwcAvg = liwcAvg[liwcAvg["Avg_Tone"].notna()]
liwcAvg.to_csv("LIWC_Avg_Pruned.csv", index=True, encoding='utf8')
