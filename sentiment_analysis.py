import pandas
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")

scores = []
df = pandas.read_csv("data/preprocessed_data.csv")

def checkPunctuation(title):
    last = title[-1]
    if last == "." or last == "?" or last == "!":
        return title
    else:
        return title + "."

for title in df["Title"]:
    body = df["Text"]
    body = "" if pandas.isna(body) else body
    full_text = checkPunctuation(title) + " " + body
    polarity_score = SentimentIntensityAnalyzer().polarity_scores(full_text)
    scores.append(polarity_score)

