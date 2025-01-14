import pandas

df = pandas.read_csv("data/raw_data.csv")

for index, row in df.iterrows():
    column = row["Text"]
    