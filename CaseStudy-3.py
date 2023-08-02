import seaborn as sns
import pandas as pd 
import numpy as np

pd.set_option("display.max_columns", 500)
pd.set_option("display.max_rows", 50)


data_frame = pd.read_csv("C:/Users/Ascoo/OneDrive/Masaüstü/Miuul Bootcamp/Miuul_CaseStudy/KuralTabanlSnflandrma-230620-161541/persona.csv")

df = data_frame.copy()


def uniq(dataframe,col):
    print("################################################")
    print(f"Unique values :{dataframe[col].unique()} ")
    print("################################################")
    print("Unique values frakans:\n",dataframe[col].value_counts())

uniq(df,"SOURCE")

# Prıce değişkenine göre groupby işlemi yapılır ve SOURCE değişkenine göre kırılım yapılarak değerler ifade edilir.


def groupby_func(dataframe, col, target, targetMore = False, target_2 = "COUNTRY"):
    
    if dataframe[target].dtype not in ["float64", "int64"]:
        print(dataframe.groupby(col).agg({target : ["value_counts"]}))
    else:
        print(dataframe.groupby(col).agg({target : ["sum","max","min","mean","count"]}))
    if targetMore:
        print(dataframe.groupby([target,target_2]).agg({col : ["mean"]}))

# Q4
groupby_func(df, "PRICE", "COUNTRY")

# Q5-6-8
groupby_func(df, "COUNTRY", "PRICE")

# Q7-Q9
groupby_func(df, "SOURCE", "PRICE")

# Q10

groupby_func(df, "PRICE", targetMore = True, target = "COUNTRY", target_2 = "SOURCE" )

# Q11

agg_df = df.groupby(["COUNTRY","SOURCE","SEX","AGE"]).agg({"PRICE" : "mean"}).sort_values(by="PRICE", ascending = False).reset_index()

# Mission 5

agg_df["AGE"] = agg_df["AGE"].astype("category")

agg_df["AGE_CUT"] = pd.cut(agg_df["AGE"], [0, 18, 23, 30, 40, 70], labels = ["(0_18)","(19_23)","(24_30)","(31_40)","(41_70)"])

# Mission 6
col = [col for col in agg_df.columns if col not in ["PRICE","AGE"]]

cust_level_based = agg_df[col].apply(lambda x : "_".join(x), axis =1)

agg_df.insert(0,"customers_level_based",cust_level_based)

drop_list = col + ["AGE"]

agg_df.drop(drop_list, axis=1, inplace = True)

# Mission 7

agg_df["PRICE_CUT"] = pd.qcut(agg_df["PRICE"], 4,  labels = ["Cheap","Normal","leastExpensive","QuiteExpensive"])

agg_df.groupby("PRICE_CUT").agg({"PRICE":["mean","sum","max"]})


# Mission 8

new_user = "tur_android_female_(31_40)"
new_user_fr = "fra_ios_female_(31_40)"

agg_df.groupby(agg_df.loc[(agg_df["customers_level_based"] == new_user),"PRICE_CUT"]).agg({"PRICE": "mean"})

agg_df.groupby([agg_df.loc[agg_df["customers_level_based"] == new_user_fr,"PRICE_CUT"]]).agg({"PRICE":"mean",
                                                                                              "PRICE_CUT" : "count"})

