#User Lookup Data Pruning + Export
import pandas as pd
data = pd.read_json("User_Lookup_Data_2.0.json", dtype={}, lines=True)
data.drop(["possibly_sensitive", "reply_settings", "context_annotations", "attachments", "entities", "conversation_id", "public_metrics", "geo", "source", "__twarc", "author"], axis=1, inplace = True)
data = data[data['referenced_tweets'].isnull()]
data = data[data['in_reply_to_user_id'].isnull()]
data = data[data.lang == 'en']
data.drop(["lang", "in_reply_to_user_id", "in_reply_to_user", "withheld", "referenced_tweets"], axis=1, inplace = True)

valueData = data['author_id'].value_counts().rename_axis('unique_values').reset_index(name='counts')
valueData.to_csv("User_Look_Value_Count.csv", index=True, encoding='utf8')