import pandas as pd
data = pd.read_json("Twarc_Test_Bed_Data.json", lines=True)
data.drop(["possibly_sensitive", "reply_settings", "context_annotations", "referenced_tweets", "entities", "lang", "in_reply_to_user_id", "conversation_id", "public_metrics", "geo", "source", "in_reply_to_user", "__twarc"], axis=1, inplace = True)
data.to_csv("Test_Bed_Pandas_Output.csv", index=False, encoding='utf8')