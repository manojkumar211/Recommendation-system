import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data import df


df.dropna(inplace=True,ignore_index=True)

title_list=df['title'].tolist()