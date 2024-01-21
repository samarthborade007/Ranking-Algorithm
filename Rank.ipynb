import numpy as np

# Sample data representing recommendations from your initial model
recommendations = [
    {"song_id": 1, "popularity": 80, "artist": "Artist1", "artist_popularity": 90, "genre": "Pop", "decade": 2000},
    {"song_id": 2, "popularity": 70, "artist": "Artist2", "artist_popularity": 85, "genre": "Rock", "decade": 1990},
    # Add more recommendations as needed
]

# New input song
input_song = {"song_id": 3, "popularity": 90, "artist": "Artist2", "artist_popularity": 85, "genre": "Rock", "decade": 2000}

# User preferences (weights for each parameter)
weights = {
    "popularity": 0.1,
    "artist_popularity": 0.1,
    "artist": 0.2,
    "genre": 0.3,
    "decade": 0.2,
}

# Add the new input song to recommendations
recommendations.append(input_song)

# Separate the input song from recommendations
input_song_index = len(recommendations) - 1
input_song = recommendations.pop(input_song_index)

def calculate_similarity_score(song1, song2, weights):
    # Calculate the similarity score between two songs based on the assigned weights
    similarity_score = sum(weights[parameter] * float(song1[parameter] == song2[parameter]) for parameter in weights)
    return similarity_score

def rank_songs(recommendations, input_song, weights):
    # Calculate similarity scores
    for recommendation in recommendations:
        recommendation['similarity_score'] = calculate_similarity_score(input_song, recommendation, weights)

    # Rank songs based on similarity scores
    ranked_songs = sorted(recommendations, key=lambda x: x['similarity_score'], reverse=True)

    return ranked_songs

# Example usage
ranked_songs = rank_songs(recommendations, input_song, weights)

# Display the top-ranked songs with scores rounded to 2 decimal places
for i, song in enumerate(ranked_songs):
    print(f"{i + 1}. Song {song['song_id']} - Similarity Score: {round(song['similarity_score'], 2)}")
