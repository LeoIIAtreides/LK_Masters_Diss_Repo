import pandas as pd
data = pd.read_json("User_Lookup_Data.json", lines=True)
data.drop(["possibly_sensitive", "reply_settings", "context_annotations", "attachments", "entities", "lang", "conversation_id", "public_metrics", "source", "__twarc"], axis=1, inplace = True)
data.to_csv("LIWC_Input_Data.csv", index=True, encoding='utf8')