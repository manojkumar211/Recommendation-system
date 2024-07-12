import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# Load the dataset:

df=pd.read_csv("C:/AI&ML Engineer/Projects/Recommendation System/movies.csv")


class data:

    try:

        df_head=df.head()
        df_tail=df.tail()
        df_dup=df.duplicated()
        df_null=df.isnull().sum()
        df_shap=df.shape

    except Exception as e:
        raise Exception(f"Error find in data level :\n"+str(e))

    def __init__(self,df_head,df_tail,df_dup,df_null,df_shap):

        try:

            self.df_head=df_head
            self.df_tail=df_tail
            self.df_dup=df_dup
            self.df_null=df_null
            self.df_shap=df_shap

        except Exception as e:
            raise Exception(f"Erroir find at initiat level :\n"+str(e))
        
    try:

        def df_head_defin(self):
            return self.df_head
        
        def df_tail_defin(self):
            return self.df_tail
        
        def df_dup_defin(self):
            return self.df_dup
        
        def df_null_defin(self):
            return self.df_null
        
        def df_shapp_defin(self):
            return self.df_shap
        
    except Exception as e:
        raise Exception(f"Error find in define level :\n"+str(e))
    
