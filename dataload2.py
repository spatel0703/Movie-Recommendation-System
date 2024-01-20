# app/dataloader.py
import pandas as pd

class DataLoader2:
    @staticmethod
    def load_data():
        moviesdf = pd.read_csv(r'C:\Users\shrey\OneDrive\Documents\Movie recommendation System\tmdb_5000_movies.csv',
                               na_filter=False)
        creditsdf = pd.read_csv(r'C:\Users\shrey\OneDrive\Documents\Movie recommendation System\tmdb_5000_credits.csv',
                                na_filter=False)
        return moviesdf, creditsdf

    @staticmethod
    def preprocess_data(moviesdf, creditsdf):
        # Merge movies and credits DataFrames on the 'id' column
        moviesdf = pd.merge(moviesdf, creditsdf, left_on='id', right_on='movie_id', suffixes=('_movies', '_credits'))

        # Combine relevant text columns for TF-IDF vectorization
        moviesdf['combined_features'] = moviesdf['genres'] + ' ' + moviesdf['keywords'] + ' ' + moviesdf[
            'overview'] + ' ' + moviesdf['cast'] + ' ' + moviesdf['crew']

        # Replace missing values with empty strings
        moviesdf['combined_features'] = moviesdf['combined_features'].fillna('')

        return moviesdf
