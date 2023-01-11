# DataScience

This code is for a Netflix recommendation engine. It first loads the data from a CSV file using  -> 
pandas, a Python library for data manipulation and analysis.
The data contains information about movies and TV shows on Netflix, such as the cast, director, production country, and genres.

The code then removes any rows with missing values in the 'Cast', 'Production Country' and 'Rating' columns. This is done by calling the dropna() function on the DataFrame.

Then the code splits the dataset into two parts, one for movies and the other for TV shows. This is done by filtering the data by the Content Type column, extracting the rows where the type is 'Movie' or 'TV Show' using the comparison operator ==. Then it drops columns that aren't useful for the analysis. The resulting two dataframes are movies and tvShows.

Next, the code uses a for loop to iterate through the 'Cast' column of the movies DataFrame, and uses a regular expression to split each entry in the column on a comma and whitespace. This creates a list of lists, with each sublist containing the actors in a given movie.

The next step is to create a binary matrix, where each row corresponds to a movie, and each column corresponds to an actor. The value in a cell is 1 if the actor is in the corresponding movie and 0 otherwise. This is done using two nested for loops, iterating through the actors in the movie and the actors in the actorsList, checking if each actor is in the movie, and appending 1 or 0 accordingly to the actors_c binary matrix.

The same process is repeated for the 'Director', 'Production Country' and 'Genres' columns as well.

At the end, the matrix is transposed using the transpose() method to make it more suitable for further analysis.
The final DataFrames are actors_c, directors_c, countries_c, genres_c.
