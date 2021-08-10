#
import pandas as pd
data = pd.read_json("Twarc_Test_Bed_Data_2.json", lines=True)
data.drop(["possibly_sensitive", "reply_settings", "context_annotations", "attachments", "entities", "lang", "conversation_id", "public_metrics", "geo", "source", "author", "__twarc"], axis=1, inplace = True)
data['author_id'].value_counts()
valueData = data['author_id'].value_counts().rename_axis('unique_values').reset_index(name='counts')
valueData.to_csv("Value_Count_Data.csv", index=True, encoding='utf8')