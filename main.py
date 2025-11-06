import os
os.environ["ORT_LOGGING_LEVEL"] = "ERROR"
os.environ["CHROMADB_TELEMETRY_DISABLED"] = "1"
os.environ["TRANSFORMERS_NO_ADVISORY_WARNINGS"] = "1"
os.environ["TOKENIZERS_PARALLELISM"] = "false"

import warnings
warnings.filterwarnings("ignore")

from pathlib import Path
from data_generator import generate_listings
from db import load_listings, create_vector_db
from search import find_matches
from personalize import personalize_listing

def run():
    print("----------------------")
    print("HomeMatch running. Search for property you need.")
    print("----------------------\n")

    try:
        user_preferences = input("Write your preferences (leave blank for default preferences):")
    except EOFError:
        user_preferences = ""

    if not user_preferences.strip():
        user_preferences = (
            "I want a cozy 3-bedroom home in a quiet neighborhood with good schools, "
            "near parks, and with eco-friendly features like solar panels and a garden."
        )

    if not Path("listings.json").exists():
        generate_listings("listings.json")

    listings = load_listings("listings.json")
    db = create_vector_db(listings)

    matches = find_matches(db, user_preferences, k=3)

    print("\n----------------------")
    print("Here are your listings for given preferences:")
    print(user_preferences)
    print("----------------------\n")

    for i, result in enumerate(matches, start=1):
        personalized = personalize_listing(result.page_content, user_preferences)
        print(f"--- Listing #{i} ---\n")
        print(personalized)
        print("----------------------")
        print(result.page_content)
        print()

if __name__ == "__main__":
    run()
