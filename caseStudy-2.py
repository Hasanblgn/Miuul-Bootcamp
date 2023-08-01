# task 1


# Verilen string ifadenin tüm harflerini büyük hafe çeviriniz. Virgül ve nokta yerine space koyunuz ve kelimeleri ayırınız.

text = "The goal is to turn data into information, and information into insight."

txt_split = text.upper().split(" ")

final = [txt.replace(".","") for txt in txt_split]


#%%

lst = ["D","A","T","A","S","C","I","E","N","C","E"]

# 1
print(len(lst))
#2

print(lst[0],lst[10])

#3
print(lst[0:4])

#4

lst.remove(lst[8])
print(lst)
#5

lst.append("A")

print(lst)
#6

lst.insert(8,"N")

print(lst)

#%%



ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]
dct = {}
for idx, col in enumerate(ogrenciler,1):
    if idx < 4:
        dct[f"Mühendislik Fakültesi {idx}. Öğrenci"] = col
    else:
        dct[f"TIP Fakültesi {idx-3}. Öğrenci"] = col




#%%

import seaborn as sns

df = sns.load_dataset("car_crashes")


df_col = [col for col in df.columns if col != "abbrev" and col != "no_previous"]
df_new = df[df_col]

df.head()

#%%


import numpy as np

import seaborn as sns

import pandas as pd


df = sns.load_dataset("titanic")
pd.set_option("display.max_columns", 500)


df[["age", "adult_male", "alive"]]

df["Age2"] = df["age"] ** 2

df.drop("Age2", axis = 1, inplace = True)

df[:, ~df.columns.str.contains("age")].head()

df.iloc[0:3]

col_names = ["age", "embarked", "alive"]

df.loc[0:3, col_names]

df[df["age"] > 50]["age"].count()

df.loc[df["age"] > 50, ["class", "age"]].head()

df.loc[(df["sex"] == "male") & (df["age"] < 25), ["class", "age"]].head()

df_new = df.loc[(df["sex"] == "male") &
           (df["age"] < 25) &
           ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),
           ["class", "age", "embark_town"]].head()

df_new["embark_town"].value_counts()

df.groupby("sex")["age"].mean()
df.groupby(["sex","embark_town"]).agg({"age" : ["sum","mean"],
                       "survived" : "mean",
                       "sex" : "count"})


df.pivot_table("survived","sex",["embarked", "class"])

df.groupby(["sex","embark_town","class"]).agg({"age": ["mean"],
                                               "survived" : "mean",
                                               "sex" : "count"})


df["new_df"]  = pd.cut(df["age"],[0, 10, 18, 25, 40, 90]) # a böl

df.pivot_table("survived", "sex", ["new_df", "class"])


df.loc[:, df.columns.str.contains("age")].apply(lambda x: x/10).head()

df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x-x.mean())/ (x.std())).head()



def standartScaler(colName):
    return (colName - colName.mean()) / (colName.std())

df.loc[:, df.columns.str.contains("age")].apply(standartScaler).head()

df.loc[:, df.columns.str.contains("age")] = df.loc[:,df.columns.str.contains("age")].apply(standartScaler)
df.head()

m = np.random.randint(1, 30, size =(5, 3))

df1 = pd.DataFrame(m, columns = ["var1","var2","var3"])
df2 = df1 + 99



