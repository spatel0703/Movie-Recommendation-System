# Movie-Recommendation-System

Welcome to the Movie Recommendation System project! This system leverages Python, Flask, and SQL to provide users with personalized movie recommendations based on their preferences.

## Overview

The Movie Recommendation System is designed to offer a user-friendly experience for discovering movies tailored to individual tastes. It comprises three main components:

1. **Data Management:**
   - The project utilizes a PostgreSQL database to store movie information, including details on budgets, revenues, cast, crew, and genres. The `DatabaseManager` class in Python is responsible for creating and managing these tables.

2. **Data Preprocessing:**
   - The `DataLoader2` class is responsible for loading movie data from external CSV files (`tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`). It preprocesses the data by merging movie and credit information, creating combined features for TF-IDF vectorization, and handling missing values.

3. **Recommendation Engine:**
   - The heart of the project is the `RecommendationEngine` class, which uses TF-IDF and cosine similarity to generate movie recommendations based on user input. This class interacts with the preprocessed data and provides an interface for users to input their preferences.

4. **Flask UI (Work in Progress):**
   - The Flask portion of the project is still under development and will serve as the user interface for interacting with the recommendation system. This component will allow users to input their preferences, view recommendations, and navigate the system effortlessly.

## Getting Started

To run the Movie Recommendation System on your local machine, follow these steps:

1. **Database Setup:**
   - Ensure you have a PostgreSQL database installed and running.
   - Update the database connection details in `app/database_manager.py`.

2. **Data Loading:**
   - Run `dataloader.py` to load movie data into the database.

3. **Recommendation Engine:**
   - Run `recommendation_engine.py` to set up the TF-IDF matrix and recommendation engine.

4. **Flask UI (Work in Progress):**
   - Start the Flask application to access the user interface (details to be added upon completion).

## Project Structure

- `app/`: Contains the main Python modules for data management, data loading, recommendation engine, and Flask UI.
- `data/`: Placeholder for external CSV files with movie data.
- `templates/`: Planned location for HTML templates in the Flask UI.

## Future Improvements

- Complete the Flask user interface to provide an interactive experience for users.
- Enhance user input handling in the recommendation engine.
- Implement input validation and error handling throughout the code.
- Refine and optimize database queries for better performance.
- Add unit tests to ensure the reliability of the system.

## Contributing

Contributions to the Movie Recommendation System project are welcome! Feel free to open issues, submit pull requests, or provide feedback.

## License

This project is licensed under the [MIT License](LICENSE).

Happy movie recommending!
