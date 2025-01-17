import pandas

df = pandas.read_csv("data/raw_data.csv")

df = df.rename(columns={"Datetime":"Date"})
df.drop("Unnamed: 0", axis=1, inplace=True)

excluded_chars = ["\n", "*", ">", "#"]
for replace in excluded_chars:
    df["Text"] = df["Text"].str.replace(replace, "")


def cleanDate(original):
    return str(original).split()[0]

df["Date"] = df["Date"].apply(cleanDate)


df.to_csv("data/preprocessed_data.csv", index=False)

    