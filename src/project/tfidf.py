import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_cleaning import df
from sklearn.feature_extraction.text import TfidfVectorizer



tfidf_vector=TfidfVectorizer()
feature_vector=tfidf_vector.fit_transform(df['genres'])



