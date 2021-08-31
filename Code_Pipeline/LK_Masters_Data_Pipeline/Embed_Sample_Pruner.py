#Embedded Sample for sensitivity analysis
import pandas as pd

#Function to call list of high tweet vol users from: 

def get_highvol_user_list():
    highvol_user_data = pd.read_excel("10+_Value_Count_Data.xlsx")
    return highvol_user_data['unique_values'].tolist()

VADER_Avg_Pruned = pd.read_csv("Vader_Avg_Pruned.csv")
LIWC_Avg_Pruned = pd.read_csv("LIWC_Avg_Pruned.csv")

VADER_Avg_Pruned_10 = VADER_Avg_Pruned[VADER_Avg_Pruned["Author_ID"].isin(get_highvol_user_list())]
LIWC_Avg_Pruned_10 = LIWC_Avg_Pruned[LIWC_Avg_Pruned["Author_ID"].isin(get_highvol_user_list())]

VADER_Avg_Pruned_10.to_csv("VADER_Avg_Pruned_10.csv", index=True, encoding='utf8')
LIWC_Avg_Pruned_10.to_csv("LIWC_Avg_Pruned_10.csv", index=True, encoding='utf8')
