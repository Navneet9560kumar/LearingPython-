# In the lecture titled "Day 3 Personal Movie Tracker with JSON," the instructor introduces JSON (JavaScript Object Notation) as a flexible data representation format, similar to how data is organized in Excel or CSV files. The focus is on creating a Python command-line tool for managing a personal movie database, which is stored in a JSON file.

# Key points include:

# Each movie entry has three fields: title, genre, and rating (out of 10).
# Functionalities include adding movies, viewing all movies, searching by title or genre, and preventing duplicate entries.
# The instructor demonstrates how to work with JSON data in Python using the built-in JSON module, covering loading, saving, and ensuring effective data handling.
# Error handling is emphasized, especially regarding duplicate titles and user input validation.
# Practical coding examples are provided, illustrating how to develop functions for managing movie entries and efficient data retrieval with list comprehensions.
# The lecture concludes with a demonstration of the completed movie tracker tool and encourages learners to experiment with the code while highlighting modular programming practices for better software development.

# If you have any specific questions about this lecture or need further clarification on any points, feel free to ask!

# Was this content relevant to you?



import os
import json
from unittest import result

FILENAME = "movies.json"

def load_movies():
      if not os.path.exists(FILENAME):
            return []
      with open(FILENAME, 'r', encoding='utf-8') as f:
            return json.load(f)
      

def save_movies(movies):
      with open(FILENAME, 'w', encoding='utf-8') as f:
            json.dump(movies, f, indent=2)



def save_movie(movies):
    title = input("Enter movie name:").strip().lower()

    if any(movie['title'].lower() == title for movie in movies):
        print("Movie already exists")
        return

    genre = input("Genre: ").strip().lower()  # ✅ Corrected here

    try:
        rating = float(input("Rating (out of 10): ").strip())
        if not (0 <= rating <= 10):
            raise ValueError("Rating must be between 0 and 10.")
    except ValueError as e:
        print(f"Invalid input for rating: {e}")
        return

    movies.append({
        "title": title,
        "genre": genre,
        "rating": rating
    })

    save_movies(movies)



def search_movies(movies):
    term = input("Enter the title or genre: ").strip().lower()

    result = [
        movie for movie in movies
        if term in movie['title'].lower() or term in movie['genre'].lower()
    ]
    
    if not result:
        print("No matching results.")
        return

    print(f"Found {len(result)} result(s):")
    for movie in result:
        print(f"- {movie['title']} -- ({movie['genre']}, {movie['rating']}/10)")



def run_movie_db():
      movies = load_movies()


      while True:
            print("\nMovie Database Menu:")
            print("1. Add Movie")
            print("2. Search Movies")
            print("3. View All Movies")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ").strip()

            if choice == '1':
                  save_movie(movies)
            elif choice == '2':
                  search_movies(movies)
            elif choice == '3':
                  if not movies:
                        print("No movies found.")
                  else:
                        for movie in movies:
                              print(f"- {movie['title']} -- ({movie['genre']}, {movie['rating']}/10)")
            elif choice == '4':
                  print("Exiting the movie database.")
                  break
            else:
                  print("Invalid choice. Please try again.")


if __name__ == "__main__":
      run_movie_db()