import pandas as pd
import json
import nltk
import re
import csv
from tqdm import tqdm
from nltk.corpus import stopwords

# load movie.metadata.tsv
meta = pd.read_csv("movie.metadata.tsv", sep = '\t', header = None)
meta.columns = ['Movie ID', 1, 'Movie Name', 3, 4, 5, 6, 7, 'Genre']

genres = []

# convert genres to dict type
for i in meta['Genre']:
    genres.append(list(json.loads(i).values()))

meta["Genres Updated"] = genres
meta["Genre"] = meta["Genres Updated"].values

plot_summaries = []
movie_ids = []
plots = []

# load plot_summaries.txt
with open("plot_summaries.txt", 'r', encoding="utf8") as file:
       reader = csv.reader(file, dialect='excel-tab') 
       for row in tqdm(reader):
            plot_summaries.append(row)
            
for p in tqdm(plot_summaries):
    movie_ids.append(p[0])
    plots.append(p[1])

plot_data = {'Movie ID': movie_ids, 'Plot' : plots}
plot_df = pd.DataFrame(plot_data)

merged = []
meta['Movie ID'] = meta['Movie ID'].astype(str)

# merge two tables according to id
merged = pd.merge(plot_df, meta[['Movie ID', 'Movie Name', 'Genre']], on = ['Movie ID'])

def change_column_order(df, col_name, index):
    cols = df.columns.tolist()
    cols.remove(col_name)
    cols.insert(index, col_name)
    return df[cols]

merged = change_column_order(merged, 'Movie Name', 1)
merged = change_column_order(merged, 'Genre', 2)

new_plot_summaries = []

def simplify_text(text):
    text = re.sub('\'','', text)
    text = re.sub('[^a-zA-Z]',' ', text)
    text = ' '.join(text.split())
    text = text.lower()
    return text

# clean the plot
merged['Plot Updated'] = merged['Plot'].apply(lambda l: simplify_text(l))
merged['Plot'] = merged['Plot Updated'].values

merged = merged.drop(columns='Plot Updated')

# download the list of stopwords from the nltk library
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def remove_stopwords(text):
    words = text.split()
    new_text = []
    for x in words:
        if x not in stop_words:
            new_text.append(x)
    return ' '.join(new_text)

# remove stop words from the plot
merged['Plot'] = merged['Plot'].apply(lambda l: remove_stopwords(l))

# save the dataframe as csv file
merged.to_csv('preprocessed_dataset.csv', index=False)
