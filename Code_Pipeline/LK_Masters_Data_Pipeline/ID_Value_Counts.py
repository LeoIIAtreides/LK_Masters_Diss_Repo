import pandas as pd
data = pd.read_json("Keyword_Query_RAW_Data.json", dtype={}, lines=True)
data.drop(["possibly_sensitive", "reply_settings", "context_annotations", "attachments", "entities", "lang", "conversation_id", "public_metrics", "geo", "source", "__twarc", "created_at"], axis=1, inplace = True)
data['author_id'].value_counts()
valueData = data['author_id'].value_counts().rename_axis('unique_values').reset_index(name='counts')
valueData.to_csv("Value_Count_Data.csv", index=True, encoding='utf8')