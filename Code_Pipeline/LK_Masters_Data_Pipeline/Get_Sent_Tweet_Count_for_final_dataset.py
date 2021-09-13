
import pandas as pd

#Function to call list final users: 

def get_final_user_list():
    final_user_data = pd.read_excel("Final_User_List.xlsx")
    return final_user_data['User_ID'].tolist()

VADER_Count = pd.read_excel("Value_Count_Data.xlsx")

VADER_Count_Pruned = VADER_Count[VADER_Count["unique_values"].isin(get_final_user_list())]

VADER_Count_Pruned.to_excel("VADER_Count_Pruned.csv", index=True, encoding='utf8')
