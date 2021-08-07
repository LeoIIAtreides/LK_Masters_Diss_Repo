import pandas as pd
data = pd.read_json("Twarc_Test_Bed_Data_2.json", lines=True)
data.drop(["possibly_sensitive", "reply_settings", "context_annotations", "attachments", "entities", "lang", "conversation_id", "public_metrics", "geo", "source", "__twarc"], axis=1, inplace = True)
data.to_csv("Test_Bed_Pandas_Output.csv", index=False, encoding='utf8')