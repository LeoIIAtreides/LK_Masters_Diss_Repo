import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import re

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()

vaderData = pd.read_csv("VADER_Pruned_Final.csv")
vaderData.drop('Unnamed: 0', axis=1, inplace=True)
vaderData.drop('Unnamed: 0.1', axis=1, inplace=True)

scores = []
# Declare variables for scores
compound_list = []
positive_list = []
negative_list = []
neutral_list = []
for i in range(vaderData['text'].shape[0]):
#print(analyser.polarity_scores(sentiments_pd['text'][i]))
    compound = analyser.polarity_scores(vaderData['text'][i])["compound"]
    pos = analyser.polarity_scores(vaderData['text'][i])["pos"]
    neu = analyser.polarity_scores(vaderData['text'][i])["neu"]
    neg = analyser.polarity_scores(vaderData['text'][i])["neg"]
    
    scores.append({"Compound": compound,
                       "Positive": pos,
                       "Negative": neg,
                       "Neutral": neu
                  })

sentiments_score = pd.DataFrame.from_dict(scores)
vaderData = vaderData.join(sentiments_score)
vaderData.to_csv("VADER_Sent_Scores.csv", index=True, encoding='utf8')