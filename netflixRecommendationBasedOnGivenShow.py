import pandas as pd
import numpy as np
import re
import nltk
import tkinter as tk
nltk.download('stopwords')

data = pd.read_csv('netflixData.csv')
data = data.dropna(subset=['Cast', 'Production Country', 'Rating'])
# Movies Data
movies = data[data['Content Type'] == 'Movie'].reset_index()
# Drop unused columns from movies
movies = movies.drop(['index', 'Show Id', 'Content Type', 'Date Added',
                    'Release Date', 'Duration', 'Description'], axis=1)
# TV shows Data
tvShows = data[data['Content Type'] == 'TV Show'].reset_index()
# Drop unused columns from TV shows
tvShows = tvShows.drop(['index', 'Show Id', 'Content Type', 'Date Added',
            'Release Date', 'Duration', 'Description'], axis=1)

cast = []
for i in movies['Cast']:
    # The regular expression r', \s*' specifies a pattern to split the string i on.
    actor = re.split(r', \s*', i)
    cast.append(actor)

castList = []
for entry in cast:
    for actor in entry:
        castList.append(actor)

actorsList = sorted(set(castList))

actors_c = [[0] * 0 for i in range(len(set(castList)))]
for i in movies['Cast']:
   k = 0
   for j in actorsList:
       if j in i:
           actors_c[k].append(1.0)
       else:
           actors_c[k].append(0.0)
       k += 1

# Transpose method means rows becomes columns and columns becomes rows
actors_c = pd.DataFrame(actors_c).transpose()
directors = []

for i in movies['Director']:
   if pd.notna(i):
       director = re.split(r', \s*', i)
       directors.append(director)


flat_list_directors = []
for sublist in directors:
   for item in sublist:
       flat_list_directors.append(item)

directors_list = sorted(set(flat_list_directors))
directors_c = [[0] * 0 for i in range(len(set(flat_list_directors)))]
for i in movies['Director']:
   k = 0
   for j in directors_list:
       if pd.isna(i):
           directors_c[k].append(0.0)
       elif j in i:
           directors_c[k].append(1.0)
       else:
           directors_c[k].append(0.0)
       k += 1

directors_c = pd.DataFrame(directors_c).transpose()
countries = []
for i in movies['Production Country']:
   country = re.split(r', \s*', i)
   countries.append(country)

flat_list_countries = []
for sublist in countries:
   for item in sublist:
       flat_list_countries.append(item)

countries_list = sorted(set(flat_list_countries))
countries_c = [[0] * 0 for i in range(len(set(flat_list_countries)))]
for i in movies['Production Country']:
   k = 0
   for j in countries_list:
       if j in i:
           countries_c[k].append(1.0)
       else:
           countries_c[k].append(0.0)
       k += 1

countries_c = pd.DataFrame(countries_c).transpose()
genres = []
for i in movies['Genres']:
   genre = re.split(r', \s*', i)
   genres.append(genre)

flat_list_genres = []
for sublist in genres:
   for item in sublist:
       flat_list_genres.append(item)

genres_list = sorted(set(flat_list_genres))
genres_c = [[0] * 0 for i in range(len(set(flat_list_genres)))]
for i in movies['Genres']:
   k = 0
   for j in genres_list:
       if j in i:
           genres_c[k].append(1.0)
       else:
           genres_c[k].append(0.0)
       k += 1

genres_c = pd.DataFrame(genres_c).transpose()
ratings = []
for i in movies['Rating']:
   ratings.append(i)

ratings_list = sorted(set(ratings))
binary_ratings = [[0] * 0 for i in range(len(set(ratings_list)))]
for i in movies['Rating']:
   k = 0
   for j in ratings_list:
       if j in i:
           binary_ratings[k].append(1.0)
       else:
           binary_ratings[k].append(0.0)
       k += 1

binary_ratings = pd.DataFrame(binary_ratings).transpose()
binary = pd.concat([actors_c, directors_c,
                  countries_c, genres_c], axis=1, ignore_index=True)
actors_2 = []
for i in tvShows['Cast']:
  actor2 = re.split(r', \s*', i)
  actors_2.append(actor2)

flat_list_actors_2 = []
for sublist in actors_2:
   for item in sublist:
       flat_list_actors_2.append(item)

actors_list_2 = sorted(set(flat_list_actors_2))
binary_actors_2 = [[0] * 0 for i in range(len(set(flat_list_actors_2)))]
for i in tvShows['Cast']:
   k = 0
   for j in actors_list_2:
       if j in i:
           binary_actors_2[k].append(1.0)
       else:
           binary_actors_2[k].append(0.0)
       k += 1

binary_actors_2 = pd.DataFrame(binary_actors_2).transpose()
countries_2 = []
for i in tvShows['Production Country']:
   country2 = re.split(r', \s*', i)
   countries_2.append(country2)

flat_list_countries_2 = []
for sublist in countries_2:
   for item in sublist:
       flat_list_countries_2.append(item)

countries_list_2 = sorted(set(flat_list_countries_2))
binary_countries_2 = [[0] * 0 for i in range(len(set(flat_list_countries_2)))]
for i in tvShows['Production Country']:
   k = 0
   for j in countries_list_2:
       if j in i:
           binary_countries_2[k].append(1.0)
       else:
           binary_countries_2[k].append(0.0)
       k += 1

binary_countries_2 = pd.DataFrame(binary_countries_2).transpose()
genres_2 = []
for i in tvShows['Genres']:
   genre2 = re.split(r', \s*', i)
   genres_2.append(genre2)

flat_list_genres_2 = []
for sublist in genres_2:
   for item in sublist:
       flat_list_genres_2.append(item)

genres_list_2 = sorted(set(flat_list_genres_2))
binary_genres_2 = [[0] * 0 for i in range(len(set(flat_list_genres_2)))]
for i in tvShows['Genres']:
   k = 0
   for j in genres_list_2:
       if j in i:
           binary_genres_2[k].append(1.0)
       else:
           binary_genres_2[k].append(0.0)
       k += 1

binary_genres_2 = pd.DataFrame(binary_genres_2).transpose()
ratings_2 = []
for i in tvShows['Rating']:
   ratings_2.append(i)

ratings_list_2 = sorted(set(ratings_2))
binary_ratings_2 = [[0] * 0 for i in range(len(set(ratings_list_2)))]
for i in tvShows['Rating']:
   k = 0
   for j in ratings_list_2:
       if j in i:
           binary_ratings_2[k].append(1.0)
       else:
           binary_ratings_2[k].append(0.0)
       k += 1

binary_ratings_2 = pd.DataFrame(binary_ratings_2).transpose()
binary_2 = pd.concat([binary_actors_2, binary_countries_2,
                    binary_genres_2], axis=1, ignore_index=True)

window = tk.Tk()
window.geometry('700x550')
window.title("Netflix Movie Recommendation")
# label maintains the labelling of each widget
header = tk.Label(window, text='Enter Movie / TV Show on Netflix For Recommendations',
                  fg="White", bg="Red", font=("Arial", 15),)
# pack() method describes the label we created on the screen
header.pack(pady=20)

def netflix_recommender(search):
   cs_list = []
   binary_list = []

   if search in movies['Title'].values:
       idx = movies[movies['Title'] == search].index.item()
       for i in binary.iloc[idx]:
           binary_list.append(i)

       point_1 = np.array(binary_list).reshape(1, -1)
       point_1 = [val for sublist in point_1 for val in sublist]
       for j in range(len(movies)):
           binary_list_2 = []
           for k in binary.iloc[j]:
               binary_list_2.append(k)
           point_2 = np.array(binary_list_2).reshape(1, -1)
           point_2 = [val for sublist in point_2 for val in sublist]
           dot_product = np.dot(point_1, point_2)
           norm_1 = np.linalg.norm(point_1)
           norm_2 = np.linalg.norm(point_2)
           cos_sim = dot_product / (norm_1 * norm_2)
           cs_list.append(cos_sim)

       movies_copy = movies.copy()
       movies_copy['cos_sim'] = cs_list
       results = movies_copy.sort_values('cos_sim', ascending=False)
       results = results[results['title'] != search]
       top_results = results.head(5)
       return (top_results)

   elif search in tvShows['Title'].values:
       idx = tvShows[tvShows['Title'] == search].index.item()
       for i in binary_2.iloc[idx]:
           binary_list.append(i)

       point_1 = np.array(binary_list).reshape(1, -1)
       point_1 = [val for sublist in point_1 for val in sublist]
       for j in range(len(tvShows)):
           binary_list_2 = []
           for k in binary_2.iloc[j]:
               binary_list_2.append(k)

           point_2 = np.array(binary_list_2).reshape(1, -1)
           point_2 = [val for sublist in point_2 for val in sublist]
           dot_product = np.dot(point_1, point_2)
           norm_1 = np.linalg.norm(point_1)
           norm_2 = np.linalg.norm(point_2)
           cos_sim = dot_product / (norm_1 * norm_2)
           cs_list.append(cos_sim)

       tv_copy = tvShows.copy()
       tv_copy['cos_sim'] = cs_list
       results = tv_copy.sort_values('cos_sim', ascending=False)
       results = results[results['Title'] != search]
       top_results = results.head(5)
       return (top_results)

   else:
       return ('Title not in dataset. Please check spelling.')


def call_recommender():
  subject = text.get()
  recommendation = netflix_recommender(subject)
  txt = ''
  tk.Frame()
  for i in recommendation.iterrows():
      txt += 'Title: ' + str(i[1][0]) + '\n'
  tk.Label(window, text=txt, fg="Red", font="Italic 15").place(x=195, y=150)


text = tk.StringVar()
tk.Entry(window, textvariable=text).place(x=100, y=90, height=30, width=290)
tk.Button(window, text='Find Recommendations',command=call_recommender).place(x=460, y=90)
window.mainloop()
