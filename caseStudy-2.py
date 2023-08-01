import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("persona.csv")



def summary(df,col = "SEX", plot=False):
    print("###############")
    print(df.info())
    print(" ")
    
    print("###############")
    print(df.head())
    print(" ")

    print("###############")
    print(df.columns)
    print(" ")
    
    
    print("###############")
    print(df.describe().T)
    print(" ")
    
    print("###############")
    print(df[col].unique())
    print(" ")
    
    if df[col].dtype in ["O","C"]:
        print("###############")
        print(df[col].value_counts())
        print(" ")
        if plot:
            print(df[col].value_counts().plot(kind="bar"))
            plt.show()
        
def compared(dataframe,target,base, *args):
    if dataframe[base].dtype in ["O","C"]:
        print(dataframe.groupby(target).agg({base : ["count"],
                                             args : ["count"]}))
    else:
        print(dataframe.groupby(target).agg({base : ["mean"],
                                           args : ["mean"]}))
        
# summary(df,"COUNTRY")
compared(df,"COUNTRY","PRICE")