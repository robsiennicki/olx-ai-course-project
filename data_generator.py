from config import get_openai_client

def generate_listings(output_path="listings.json"):
    client = get_openai_client()
    prompt = """Generate 10 diverse, realistic real estate listings with this format:
Neighborhood:
Price:
Bedrooms:
Bathrooms:
House Size:
Description:
Neighborhood Description:
Each listing should be 3-5 sentences and reflect different lifestyles."""
    response = client.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    text = response["choices"][0]["message"]["content"]
    with open(output_path, "w") as f:
        f.write(text)
    return output_path
