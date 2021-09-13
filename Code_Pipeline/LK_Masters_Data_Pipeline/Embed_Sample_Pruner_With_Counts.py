#Embedded Sample for sensitivity analysis
import pandas as pd

#Function to call list of high tweet vol users from: 

def get_highvol_user_list():
    highvol_user_data = pd.read_excel("10+_Value_Count_Data.xlsx")
    return highvol_user_data['unique_values'].tolist()


Users_With_Counts = pd.read_excel("Final_User_List_With_Counts.xlsx")


Users_With_Counts_10 = Users_With_Counts[Users_With_Counts["ID"].isin(get_highvol_user_list())]

Users_With_Counts_10.to_csv("Users_With_Counts_10.csv", index=True, encoding='utf8')
