# Enter your account information
import asyncio
import os
from idlelib import query

import pandas as pd
from twikit import Client

#USERNAME = '@vericekici123'
#EMAIL = 'sadojic896@bamsrad.com'
#PASSWORD = 'istatistik'

USERNAME = '@istatistik2027'
EMAIL = 'ertowghan@gmail.com'
PASSWORD = 'istatistik'

client = Client('tr-TR')

tweet_data = []

dates = ['. lang:tr since:2024-05-20 until:2024-05-21',
        '. lang:tr since:2024-05-29 until:2024-05-30',
        '. lang:tr since:2024-06-03 until:2024-06-04',
        '. lang:tr since:2024-06-12 until:2024-06-13',
        '. lang:tr since:2024-06-18 until:2024-06-19',
        '. lang:tr since:2024-06-27 until:2024-06-28',
        '. lang:tr since:2024-07-03 until:2024-07-04',
        '. lang:tr since:2024-07-12 until:2024-07-13',
        '. lang:tr since:2024-07-15 until:2024-07-16',
        '. lang:tr since:2024-07-26 until:2024-07-27',
        '. lang:tr since:2024-07-31 until:2024-08-01',
        '. lang:tr since:2024-08-05 until:2024-08-06',
        '. lang:tr since:2024-08-13 until:2024-08-14',
        '. lang:tr since:2024-08-22 until:2024-08-23',
        '. lang:tr since:2024-08-28 until:2024-08-29',
        '. lang:tr since:2024-09-02 until:2024-09-03',
        '. lang:tr since:2024-09-13 until:2024-09-14',
        '. lang:tr since:2024-09-17 until:2024-09-18',
        '. lang:tr since:2024-09-26 until:2024-09-27',
        '. lang:tr since:2024-10-03 until:2024-10-04',
        '. lang:tr since:2024-10-08 until:2024-10-09',
        '. lang:tr since:2024-10-16 until:2024-10-17',
        '. lang:tr since:2024-10-24 until:2024-10-25',
        '. lang:tr since:2024-10-30 until:2024-10-31',
        '. lang:tr since:2024-11-07 until:2024-11-08',
        '. lang:tr since:2024-11-13 until:2024-11-14'
        '. lang:tr since:2024-11-20 until:2024-11-21',
        '. lang:tr since:2024-11-25 until:2024-11-26',
        '. lang:tr since:2024-12-04 until:2024-12-05']

dates2 =['. lang:tr since:2024-11-20 until:2024-11-21',
        '. lang:tr since:2024-11-25 until:2024-11-26',
        '. lang:tr since:2024-12-04 until:2024-12-05',
        '. lang:tr since:2024-12-12 until:2024-12-13',
        '. lang:tr since:2024-12-18 until:2024-12-19',
        '. lang:tr since:2024-12-26 until:2024-12-27',
        '. lang:tr since:2024-12-30 until:2024-12-31',
        '. lang:tr since:2025-01-08 until:2025-01-09',
        '. lang:tr since:2025-01-13 until:2025-01-14',
        '. lang:tr since:2025-01-24 until:2025-01-25']

dates3 = ['. lang:tr since:2025-01-28 until:2025-01-29',
        '. lang:tr since:2025-02-06 until:2025-02-07',
        '. lang:tr since:2025-02-10 until:2025-02-11',
        '. lang:tr since:2025-02-20 until:2025-02-21',
        '. lang:tr since:2025-02-27 until:2025-02-28',
        '. lang:tr since:2025-03-05 until:2025-03-06']

dates4 = ['. lang:tr since:2025-03-11 until:2025-03-12',
        '. lang:tr since:2025-03-20 until:2025-03-21',
        '. lang:tr since:2025-03-26 until:2025-03-27',
        '. lang:tr since:2025-04-01 until:2025-04-02',
        '. lang:tr since:2025-04-10 until:2025-04-11',
        '. lang:tr since:2025-04-16 until:2025-04-17',
        '. lang:tr since:2025-04-23 until:2025-04-24',
        '. lang:tr since:2025-04-30 until:2025-05-01',
        '. lang:tr since:2025-05-08 until:2025-05-09',
        '. lang:tr since:2025-05-13 until:2025-05-14']

async def main():
    cookies_path = 'cookies.json'

    if os.path.exists(cookies_path):
        try:
            client.load_cookies(cookies_path)
            print('Çerezler yüklendi.')
        except Exception as e:
            print(f'Çerez yüklenirken hata oluştu: {e}')
            await client.login(
                auth_info_1=USERNAME,
                auth_info_2=EMAIL,
                password=PASSWORD,
                cookies_file=cookies_path
            )
            print('Giriş yapıldı ve çerezler kaydedildi.')
    else:
        await client.login(
            auth_info_1=USERNAME,
            auth_info_2=EMAIL,
            password=PASSWORD,
            cookies_file=cookies_path
        )
        print('Giriş yapıldı ve çerezler kaydedildi.')

    async def search_tweets(query): #örnek query '. lang:tr since:2025-04-01 until:2025-04-02'
        tweets = await client.search_tweet(query, 'Top', 10)
        if len(tweets) > 0:
            print("tweet bulundu")
        for tweet in tweets:
            tweet_data.append(
                {'id': tweet.id, 'name': tweet.user.name, 'screen_name': tweet.user.screen_name, 'Date': tweet.created_at,
                 'Text': tweet.text, 'Hashtags': tweet.hashtags, 'Views': tweet.view_count, 'Likes': tweet.favorite_count,
                 'Retweets': tweet.retweet_count, 'Replies': tweet.reply_count, "type": 'haftalik'})

    for date in dates2:
        await search_tweets(date)

    #await search_tweets(". lang:tr since:2024-05-20 until:2024-05-21")
    df = pd.DataFrame(tweet_data)
    df.to_excel('haflatik1.xlsx', index=False)


asyncio.run(main())