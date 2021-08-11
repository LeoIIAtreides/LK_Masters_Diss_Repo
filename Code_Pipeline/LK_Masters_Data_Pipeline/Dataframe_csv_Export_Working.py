import pandas as pd
data = pd.read_json("Keyword_Query_RAW_Data.json", dtype={}, lines=True)
data.drop(["possibly_sensitive", "reply_settings", "context_annotations", "attachments", "entities", "lang", "conversation_id", "public_metrics", "geo", "source", "__twarc", "created_at", "author"], axis=1, inplace = True)
data.to_csv("Pre_Processed_Data.csv", index=True, encoding='utf8')