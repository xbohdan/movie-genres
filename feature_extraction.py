import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

movies = pd.read_csv("preprocessed_dataset.csv")

vectorizer = CountVectorizer(ngram_range=(1,2), max_features=10000, max_df=0.8)
X = vectorizer.fit_transform(movies['Plot'].to_list())

movies['Feature'] = movies['Plot']

for idx, feature in enumerate(X.toarray()):
    movies['Feature'][idx] = feature

movies = movies.drop(columns='Plot')

movies.to_csv('feature_dataset.csv', index=False)