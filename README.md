# About Dataset:-
```
- In this data set we are having 3 columns, those are Index, Genres and titles.
['index', 'genres', 'title']
- We are having total 4693 rows and 3 columns.
```

# Data Cleaning:-
```
- We find 27 null/missing values in this dataset.
-  We dont have any duplicates in this dataset.
- We removied those null/missing values from the original dataset.
```
# Tf-Idf:-
```
- We used Tf-Idf Vectorization technique to make the text data into numerical data.
```
# Cosine Similarity:-
```
- To calculate the how much similarity it has in the form of percentage.
- Made the title column from data frame into list.
- Made the cosine similarity variable into list and added index values with help of enumarate function.
- Again we sorted the cosine similarity variable which is recently added index values.
```
# Difflib:-
```
- Applyed Difflib to get the closest match along with the title and genres.
- Made the closest match into index values.
```
# Output:-
```
- By using for loop we can identify the most closest matches.
```
