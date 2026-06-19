import requests
import json

# Fetch 10 posts
url = "https://jsonplaceholder.typicode.com/posts?_limit=10"

response = requests.get(url)

# Convert response to Python list
posts = response.json()

# Save to a JSON file
with open("fetched_post.json", "w") as file:
    json.dump(posts, file, indent=4)

print("10 posts saved to posts.json")