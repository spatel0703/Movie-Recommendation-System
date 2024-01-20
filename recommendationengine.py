# app/recommendation_engine.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from dataload2 import DataLoader2

class RecommendationEngine:
    def __init__(self, moviesdf, tfidf_vectorizer, tfidf_matrix):
        self.moviesdf = moviesdf
        self.tfidf_vectorizer = tfidf_vectorizer
        self.tfidf_matrix = tfidf_matrix

    def get_recommendations_by_user_input(self, top_n=10):
        # Ask the user for input
        search_criteria = input("Enter search criteria (e.g., movie title, cast member, genre): ").split(',')

        # Validate input
        if not search_criteria:
            print("Invalid search criteria. Please provide valid input.")
            return None

        # Combine user input into a single query string
        query = ' & '.join([f'combined_features.str.contains("{value}", case=False)' for value in search_criteria])

        # Filter movies based on user input
        filtered_movies = self.moviesdf.query(query)

        if filtered_movies.empty:
            print("No movies found for the given criteria.")
            return None

        # Compute TF-IDF for the filtered movies
        tfidf_matrix_filtered = self.tfidf_vectorizer.transform(filtered_movies['combined_features'])

        # Compute the cosine similarity matrix for the filtered movies
        cosine_sim_filtered = linear_kernel(tfidf_matrix_filtered, self.tfidf_matrix)

        # Get indices of movies sorted by similarity
        idx = list(filtered_movies.index)
        sim_scores = list(enumerate(cosine_sim_filtered[0]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[:top_n]

        # Check if there are any recommendations
        if not sim_scores:
            print("No recommendations found for the given criteria.")
            return None

        # Get recommended movie titles
        recommendations = self.moviesdf.iloc[[i[0] for i in sim_scores]]['original_title'].tolist()

        return recommendations

# Example usage:
if __name__ == "__main__":
    data_loader = DataLoader2()
    moviesdf, creditsdf = data_loader.load_data()
    moviesdf = data_loader.preprocess_data(moviesdf, creditsdf)

    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(moviesdf['combined_features'])

    # Create an instance of RecommendationEngine
    recommendation_engine = RecommendationEngine(moviesdf, tfidf_vectorizer, tfidf_matrix)

    # Call the method using the instance
    recommendations = recommendation_engine.get_recommendations_by_user_input()
    if recommendations:
        print(f"Recommendations based on user input: {recommendations}")
