import pandas as pd

movie_df  = pd.read_csv('movies.csv')
movie_links_df = pd.read_csv('movie_links.csv')

#print(movie_links_df.head())

print("movie_df shape", movie_df.shape)
print("movie_links_df", movie_links_df.shape)

movie_df.info()
movie_links_df.info()

final_df = pd.merge(movie_df, movie_links_df, on = "original_title")

final_df.info()

final_df.to_csv('final.csv')