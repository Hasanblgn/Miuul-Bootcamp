import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

df = sns.load_dataset("titanic")
df = df.copy()
df.head()

# # gorev2
# print("####################### gorev 1 ###########################")
# print(df.loc[:,df.columns.str.contains("sex")].value_counts())


# def unique_values(df,col):

#     print(" ")
#     print("#######################")
#     print(f"unique values : {col} ####")
#     print(df[col].unique())

# for col in df.columns:
#     unique_values(df, col)

# # gorev 6

# df.info()

# df["embarked"] = df["embarked"].astype("category")

#gorev 7

# df.loc[(df["embarked"] == "C"),:]

# görev 8

# df.loc[~(df["embarked"] == "S"),:]

# görev 9

# df.loc[(df["age"] < 30),:]

# görev 10

# df.loc[((df["fare"] > 500) | (df["age"] > 70)),:]

# görev 11

# df.isna().sum()

# görev 12

# df.drop(["who"],axis = 1)

# görev 13

# df["deck"].fillna(df["deck"].mode()[0], inplace = True)

# df["deck"].isna().sum()

# görev 14

# df["age"].fillna(df["age"].median(), inplace = True)

# görev 15

# df.groupby("survived").agg({"age":["sum","mean"],
#                         "pclass": ["count"]})

# görev 16

# df["age_flag"] = df["age"].apply(lambda x : 1 if (x <= 30) else 0)

# görev 17

# df = sns.load_dataset("tips")
# df.columns

# görev 18

# df.groupby("time").agg({"total_bill" : ["min","max"]})

# görev 19

# df.groupby(["time","day"]).agg({"total_bill" : ["min","max","mean"]})

# görev 20

# df.groupby(["time","sex"]).agg({"total_bill" : ["mean", "max", "min"]})

# görev 21

# df.loc[(df["size"] < 3) & (df["total_bill"] > 10)]["total_bill"].mean()

# görev 22

# df["total_bill_tip_sum"] = df["tip"] + df["total_bill"]

# görev 23

# new_df = df.sort_values(by = "total_bill_tip_sum").head(30)










