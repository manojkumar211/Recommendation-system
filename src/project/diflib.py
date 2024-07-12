import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import difflib
from data_cleaning import df,title_list
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tfidf import feature_vector
from cosine_similarity import cosine_similar,simitar_score,sorted_similar_movies


movie_name=input("Enter the movie name :")

close_match=difflib.get_close_matches(movie_name,title_list)

index_movie=df[df['title']==close_match[0]]['index'].values[0]



