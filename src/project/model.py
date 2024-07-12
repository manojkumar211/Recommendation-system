import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import difflib
from data_cleaning import df,title_list
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tfidf import feature_vector
from cosine_similarity import cosine_similar
from diflib import sorted_similar_movies


print("Movies suggested for you : \n")
i=1
for movie in sorted_similar_movies:
    index=movie[0]
    title_from_index=df[df.index==index]['title'].values[0]
    if (i<=10):
        print(i,'.',title_from_index)
    i+=1    


