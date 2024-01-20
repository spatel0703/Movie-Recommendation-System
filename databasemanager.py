# app/database_manager.py
import psycopg2
import pandas as pd

class DatabaseManager:
    def __init__(self, host, database, user, password):
        self.conn = psycopg2.connect(host="localhost", database="movie_recommendation", user="postgres", password="Reshma$0822")
        self.cursor = self.conn.cursor()

    def create_tables(self):
        # Connect to existing "movie_recommendation" database
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY,
                budget NUMERIC,
                revenue NUMERIC,  
                overview TEXT,
                genres TEXT );
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS credits (
                movie_id INTEGER PRIMARY KEY, 
                "cast" TEXT,
                crew TEXT);
        ''')

    movies_df = pd.read_csv(r'C:\Users\shrey\OneDrive\Documents\Movie recommendation System\tmdb_5000_movies.csv',
                           na_filter=False)
    credits_df = pd.read_csv(r'C:\Users\shrey\OneDrive\Documents\Movie recommendation System\tmdb_5000_credits.csv',
                            na_filter=False)
    def load_data_into_database(self, movies_df, credits_df):
        for row in movies_df.itertuples():
            self.cursor.execute('''
                INSERT INTO movies (id, budget, revenue, overview, genres)  
                VALUES (%s, %s, %s, %s, %s)''',
                               (row.id, row.budget, row.revenue, row.overview, row.genres))

        for row in credits_df.itertuples():
            self.cursor.execute('''
                INSERT INTO credits (movie_id, "cast", crew)
                VALUES (%s, %s, %s)''',
                               (row.movie_id, row.cast, row.crew))

        self.conn.commit()

    print("Data loaded successfully!")

    def close_connection(self):
        self.conn.close()
