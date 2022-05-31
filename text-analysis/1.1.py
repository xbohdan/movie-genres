import pandas as pd # for reading CSV files
import matplotlib.pyplot as plt
import nltk
from nltk import word_tokenize



plots = []
general_genres = []
specific_genres = []

# reading and parsing a csv file
dataset = pd.read_csv('preprocessed_dataset.csv')
plots = dataset["Plot"].values
general_genres = dataset["General genre"].values
specific_genres = dataset["Specific genre"].values

# declare lists for storying tokens, values of diversities and length of the plots 
tokens = [[] for i in plots]
diversities = [[] for i in plots]
length = [[] for i in plots]
nouns = [[] for i in plots]
adjectives = [[] for i in plots]
verbs = [[] for i in plots]

def count_parts_of_speech(text):
    parts = nltk.pos_tag(text)
    n = 0
    v = 0
    a = 0
    for part in parts:
        if part[1] in ("NN","NNS","NNP","NNPS") :
            #print(part)
            n += 1
        if part[1] in ("VB","VBG","VBD","VBP","VBZ"):
            v += 1
        if part[1] in ("JJ","JJR","JJS"):
            a += 1
    return n, v, a

# parsing plots into tokens (each word becomes an entry of a list)
# calculating length and diversities of each plot
i = 0
for plot in plots:
    print(i)
    tokens[i] = word_tokenize(plot)
    length[i] = len(tokens[i])
    diversities[i] = len(set(tokens[i]))/len(tokens[i])
    nouns[i], verbs[i], adjectives[i] = count_parts_of_speech(tokens[i])
    i+=1



# counts the number of films for each genre
def collect_genres(genres):
    # dictionary of genres
    genres_dict = {}
    for genre in genres:
        if genre in genres_dict:
            genres_dict[genre] += 1
        else:
            genres_dict[genre] = 1
    return genres_dict

# calculating a mean for each genre
def mean_genres(genres, values):
    # dictionary of genres
    genres_dict = {}
    genres_dict_count = {}
    i = 0
    for genre in genres:
        if genre in genres_dict:
            genres_dict[genre] += values[i]
            genres_dict_count[genre] += 1
        else:
            genres_dict[genre] = values[i]
            genres_dict_count[genre] = 1
        i += 1
    # calculating the average
    for genre in genres_dict:
        genres_dict[genre] /= genres_dict_count[genre]
    return genres_dict

# draws a distribution of values amount genres
def diagram(count_classes):
    # plt.bar(range(len(dct)), sorted(list(count_classes.values())), align='center')
    plt.bar(range(len(count_classes)), sorted(list(count_classes.values())), align='center')
    # plt.xticks(range(len(dct)), sorted(list(count_classes.keys())), rotation=90, fontsize=7)
    plt.xticks(range(len(count_classes)), sorted(list(count_classes.keys())), rotation=90, fontsize=7)
    plt.show()


#count_general_genres = collect_genres(general_genres)
#diagram(count_general_genres)

#count_specific_genres = collect_genres(specific_genres)
#diagram(count_specific_genres)

#length_general_genres = mean_genres(general_genres, length)
#diagram(length_general_genres)

#length_specific_genres = mean_genres(specific_genres, length)
#diagram(length_specific_genres)

#diversities_general_genres = mean_genres(general_genres, diversities)
#diagram(diversities_general_genres)

#diversities_specific_genres = mean_genres(specific_genres, diversities)
#diagram(diversities_specific_genres)
