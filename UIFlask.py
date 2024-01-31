from flask import Flask
from flask import render_template
from flask import request
from recommendationengine import RecommendationEngine
from dataload2 import DataLoader2
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/recommendations', methods=['POST'])
def get_recommendations():
    if request.method == 'POST':
        search_criteria = request.form['search_criteria']

        data_loader = DataLoader2()
        moviesdf, creditsdf = data_loader.load_data()
        moviesdf = data_loader.preprocess_data(moviesdf, creditsdf)

        tfidf_vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf_vectorizer.fit_transform(moviesdf['combined_features'])

        recommendation_engine = RecommendationEngine(moviesdf, tfidf_vectorizer, tfidf_matrix)

        recommendations = recommendation_engine.get_recommendations_by_user_input(search_criteria)

        return render_template('recommendations.html', recommendations=recommendations)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

