import requests
from database.mongo import users_collection, posts_collection
from models.user_model import User
from models.post_model import Post
from config import API_KEY

# Function to fetch and store users
def fetch_and_store_users():
    url = "https://dummyapi.io/data/v1/user"
    headers = {"app-id": API_KEY}

    response = requests.get(url, headers=headers)
    users_data = response.json()


    for user_data in users_data['data']:
        user = User(user_data)
        users_collection.insert_one(user.to_dict())

# Function to fetch and store posts
def fetch_and_store_posts():
    users = users_collection.find({}, {'id': 1})

    url_template = "https://dummyapi.io/data/v1/user/{}/post"
    headers = {"app-id": API_KEY}

    for user in users:
        url = url_template.format(user['id'])
        response = requests.get(url, headers=headers)
        posts_data = response.json()

        for post_data in posts_data['data']:
            post = Post(post_data)
            posts_collection.insert_one(post.to_dict())

if __name__ == "__main__":
    fetch_and_store_users()
    fetch_and_store_posts()
