import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_cleaning import df
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tfidf import feature_vector
from diflib import index_movie


cosine_similar=cosine_similarity(feature_vector)

simitar_score=list(enumerate(cosine_similar[index_movie]))

sorted_similar_movies=sorted(simitar_score,key= lambda x: x[1],reverse=True)