import asyncio
import os

import pandas as pd

from twikit import Client

###########################################

# Enter your account information
USERNAME = "@istatistik2027"
EMAIL = "ertowghan@gmail.com"
PASSWORD = "istatistik"

client = Client('tr-TR')

tweet_data = []

async def main():
    cookies_path = 'cookies.json'

    if os.path.exists(cookies_path):
        client.load_cookies(cookies_path)
        print("Çerezler yüklendi.")
    else:
        await client.login(
            auth_info_1=USERNAME,
            auth_info_2=EMAIL,
            password=PASSWORD,
            cookies_file=cookies_path
        )
        print("Giriş yapıldı ve çerezler kaydedildi.")
# Search  Tweets
"""
    tweets = await client.search_tweet('bayram since:2025-04-01 until:2025-04-02', 'Top')
    for tweet in tweets:
        tweet_data.append(
            {"id": tweet.id, "name": tweet.user.name, "screen_name": tweet.user.screen_name, "Date": tweet.created_at,
             "Text": tweet.text, "Views": tweet.view_count, "Likes": tweet.favorite_count,
             "Retweets": tweet.retweet_count, "Replies": tweet.reply_count})

    while len(tweet_data) < 100:
        tweets = await tweets.next()
        for tweet in tweets:
            tweet_data.append({"id":tweet.id, "name": tweet.user.name, "screen_name": tweet.user.screen_name, "Date":tweet.created_at, "Text":tweet.text, "Views":tweet.view_count, "Likes":tweet.favorite_count, "Retweets":tweet.retweet_count, "Replies":tweet.reply_count})
            if len(tweet_data) >= 100:
                break

    df = pd.DataFrame(tweet_data)
    df.to_excel('tweets.xlsx', index=False)
"""


"""
    ###########################################

    # Search users
    users = await client.search_user('query')
    for user in users:
        print(user)
    # Search more users
    more_users = await users.next()

    ###########################################

    # Get user by screen name
    USER_SCREEN_NAME = 'example_user'
    user = await client.get_user_by_screen_name(USER_SCREEN_NAME)

    # Access user attributes
    print(
        f'id: {user.id}',
        f'name: {user.name}',
        f'followers: {user.followers_count}',
        f'tweets count: {user.statuses_count}',
        sep='\n'
    )

    # Follow user
    await user.follow()
    # Unfollow user
    await user.unfollow()

    # Get user tweets
    user_tweets = await user.get_tweets('Tweets')
    for tweet in user_tweets:
        print(tweet)
    # Get more tweets
    more_user_tweets = await user_tweets.next()

    ###########################################

    # Send dm to a user
    media_id = await client.upload_media('./image.png', 0)
    await user.send_dm('dm text', media_id)

    # Get dm history
    messages = await user.get_dm_history()
    for message in messages:
        print(message)
    # Get more messages
    more_messages = await messages.next()

    ###########################################

    # Get tweet by ID
    TWEET_ID = '0000000000'
    tweet = await client.get_tweet_by_id(TWEET_ID)

    # Access tweet attributes
    print(
        f'id: {tweet.id}',
        f'text {tweet.text}',
        f'favorite count: {tweet.favorite_count}',
        f'media: {tweet.media}',
        sep='\n'
    )

    # Favorite tweet
    await tweet.favorite()
    # Unfavorite tweet
    await tweet.unfavorite()
    # Retweet tweet
    await tweet.retweet()
    # Delete retweet
    await tweet.delete_retweet()

    # Reply to tweet
    await tweet.reply('tweet content')

    ###########################################

    # Create tweet with media
    TWEET_TEXT = 'tweet text'
    MEDIA_IDS = [
        await client.upload_media('./media1.png', 0),
        await client.upload_media('./media2.png', 1),
        await client.upload_media('./media3.png', 2)
    ]

    client.create_tweet(TWEET_TEXT, MEDIA_IDS)

    # Create tweet with a poll
    TWEET_TEXT = 'tweet text'
    POLL_URI = await client.create_poll(
        ['Option 1', 'Option 2', 'Option 3']
    )

    await client.create_tweet(TWEET_TEXT, poll_uri=POLL_URI)

    ###########################################

    # Get news trends
    trends = await client.get_trends('news')
    for trend in trends:
        print(trend)

    ###########################################
"""

asyncio.run(main())
