from homework6.models import User, Post, Session
import aiohttp

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def fetch_users_data():
    return await fetch_json(USERS_DATA_URL)


async def fetch_posts_data():
    return await fetch_json(POSTS_DATA_URL)


async def save_data(users_data, posts_data):
    async with Session() as session:
        users = [User(id=user["id"], name=user["name"], username=user["username"], email=user["email"])
                 for user in users_data]
        posts = [Post(id=post["id"], user_id=post["userId"], title=post["title"], body=post["body"])
                 for post in posts_data]
        session.add_all(users + posts)
        await session.commit()
