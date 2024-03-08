import pandas as pd

df = pd.read_csv("./airports.csv", low_memory=False)


print(df)

print()

print(df.tail(12)["iso_country"])

print()

print(df.loc[1])

print()

print(df.iloc[1])

print()

print(df[df["iso_country"] == "PL"])

print()

print(df[df["name"] != df["municipality"]])

print()

print(df["elevation_ft"])

df["elevation_ft"] = df["elevation_ft"] * 0.3048

print()

print(df["elevation_ft"])

print()

print(df[df["iso_country"].duplicated(keep=False) == False]["iso_country"])
