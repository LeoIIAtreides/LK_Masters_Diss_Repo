import pandas as pd
data = pd.read_json("Keyword_Query_RAW_Data.json", lines=True)
data.drop(["possibly_sensitive", "reply_settings", "context_annotations", "attachments", "entities", "lang", "conversation_id", "public_metrics", "geo", "source", "__twarc"], axis=1, inplace = True)
data.to_csv("Pre_Processed_Data.csv", index=True, encoding='utf8')