import asyncio
from dotenv import load_dotenv, dotenv_values
import os
import tweepy
import tweepy.asynchronous

# Load environment variables from .env file
load_dotenv()

bearer_token = os.getenv("BEARER_TOKEN")


async def get_me(client):
    return await client.get_me()

async def main():
    client = tweepy.asynchronous.AsyncClient(bearer_token=bearer_token)
    response = await client.get_me()
    print(response.data)



if __name__ == "__main__":
    asyncio.run(main())