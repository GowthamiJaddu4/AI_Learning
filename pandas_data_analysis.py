#creating a DataFrame
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [22, 25, 23, 28],
    "Salary": [45000, 60000, 52000, 70000],
    "Department": ["IT", "HR", "IT", "Finance"]
}

df = pd.DataFrame(data)

print(df)

#creating series
ages = pd.Series([20, 21, 22, 23])

print(ages)
# if we have taken the series ,we can take the index
ages = pd.Series(
    [20, 21, 22],
    index=["Alice", "Bob", "Charlie"]
)
"""Series = 1-dimensional labeled data (usually one column)
DataFrame = 2-dimensional table (rows + columns)"""

"""
#The first basic inspection
df = pd.read_csv("data.csv")

print(df.head())
print(df.shape)
print(df.info())
print(df.describe())
head() → What does the data look like?
shape → How big is it?
columns → What information do I have?
info() → What are the data types/missing values?
describe() → What do the numbers look like?
"""


"""iloc-integer based
loc-position based
These two are used to access the rows and columns from the dataframe"""



"""Find missing values
df.isnull()
df.isnull().sum()
df.dropna()
df["Age"] = df["Age"].fillna(df["Age"].mean())
Depending on the dataset, you might:

remove rows
fill with mean/median
fill categorical values with mode
use a more advanced imputation technique

sorting values
df.sort_values("Marks")

to find merges the dataframes 
pd.merge(df1, df2, on="ID", how="inner")
pd.merge(df1, df2, on="ID", how="left")
pd.merge(df1, df2, on="ID", how="right")
pd.merge(df1, df2, on="ID", how="outer")
df.sort_values("Salary", ascending=True)   # low → high
df.sort_values("Salary", ascending=False)  # high → low
