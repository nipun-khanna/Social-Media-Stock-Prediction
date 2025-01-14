import praw
import pandas
import os
from datetime import datetime
from dotenv import load_dotenv, dotenv_values

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    user_agent="Tesla News Scrape",
)

format = {
    "Id": [],
    "Datetime": [],
    "Title": [],
    "Text": [],
    "URL": []
}

def isValid(postId):
    return postId not in format["Id"]

def appendData(post):
    format["Id"].append(post.id)
    unix_time = int(post.created_utc)
    readable_date = datetime.utcfromtimestamp(unix_time).strftime('%Y-%m-%d %H:%M:%S')
    format["Datetime"].append(readable_date)
    format["Title"].append(post.title)
    format["Text"].append(post.selftext)
    format["URL"].append(post.url)


sub = reddit.subreddit("wallstreetbets")
for post in sub.search(query="tesla", limit=1000, time_filter="year"):
    appendData(post)

for post in sub.search(query="tsla", limit=1000, time_filter="year"):
    if isValid(post.id):
        appendData(post)

for post in sub.search(query="$tsla", limit=1000, time_filter="year"):
    if isValid(post.id):
        appendData(post)


sub = reddit.subreddit("stocks")
for post in sub.search(query="tesla", limit=1000, time_filter="year"):
    appendData(post)

for post in sub.search(query="tsla", limit=1000, time_filter="year"):
    if isValid(post.id):
        appendData(post)

for post in sub.search(query="$tsla", limit=1000, time_filter="year"):
    if isValid(post.id):
        appendData(post)


sub = reddit.subreddit("investing")
for post in sub.search(query="tesla", limit=1000, time_filter="year"):
    appendData(post)

for post in sub.search(query="tsla", limit=1000, time_filter="year"):
    if isValid(post.id):
        appendData(post)

for post in sub.search(query="$tsla", limit=1000, time_filter="year"):
    if isValid(post.id):
        appendData(post)


data = pandas.DataFrame(format)
data.to_csv("data/raw_data.csv", index=True)