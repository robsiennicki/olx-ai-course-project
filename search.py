def find_matches(vector_db, preferences, k=3):
    return vector_db.similarity_search(preferences, k=k)
