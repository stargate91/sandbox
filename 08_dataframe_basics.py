import pandas as pd
import os

d={
    'name': ['Anna', 'Béla', 'Csaba'],
    'age': [21, 23, 22],
    'score': [88, 75, 101]
}

df=pd.DataFrame(d)

print(df)

df_75p = df[df['score'] > 75]

print(df_75p)

df_sv = df.sort_values(by=['age'])

print(df_sv)

age_gr = df.groupby("age")

print(age_gr)

mean = df["score"].mean() # can be used with groupby

print(mean)

unique = df["name"].nunique()

print(unique)

vcounts = df["age"].value_counts() # can be used with groupby

print(vcounts)

base_path = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_path, "08_data.csv")

output_path = os.path.join(base_path, "08_new.csv")

# print(df.head())
# print(df.info())
# print(df.describe())


df["name"] = df["name"].str.upper()
df.to_csv(output_path, index=False)