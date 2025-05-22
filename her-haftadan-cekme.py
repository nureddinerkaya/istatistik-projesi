# Enter your account information
import asyncio
import os
from datetime import datetime, timedelta
import time
from idlelib import query

import pandas as pd
from twikit import Client

#USERNAME = '@statsci123'
#EMAIL = 'wekobi3974@bamsrad.com'
#PASSWORD = 'istatistik123'

USERNAME = "@IsimGuzel123"
EMAIL = "atharva.shakil@fabricoak.com"
PASSWORD = "istatistik123"

#USERNAME = '@istatistik2027'
#EMAIL = 'ertowghan@gmail.com'
#PASSWORD = 'istatistik'

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
        '. lang:tr since:2024-10-03 until:2024-10-04']

dates2 = ['. lang:tr since:2024-10-08 until:2024-10-09',
        '. lang:tr since:2024-10-16 until:2024-10-17',
        '. lang:tr since:2024-10-24 until:2024-10-25',
        '. lang:tr since:2024-10-30 until:2024-10-31',
        '. lang:tr since:2024-11-07 until:2024-11-08',
        '. lang:tr since:2024-11-13 until:2024-11-14'
        '. lang:tr since:2024-11-20 until:2024-11-21',
        '. lang:tr since:2024-11-25 until:2024-11-26',
        '. lang:tr since:2024-12-04 until:2024-12-05',
        '. lang:tr since:2024-11-20 until:2024-11-21',
        '. lang:tr since:2024-11-25 until:2024-11-26',
        '. lang:tr since:2024-12-04 until:2024-12-05',
        '. lang:tr since:2024-12-12 until:2024-12-13',
        '. lang:tr since:2024-12-18 until:2024-12-19',
        '. lang:tr since:2024-12-26 until:2024-12-27',
        '. lang:tr since:2024-12-30 until:2024-12-31',
        '. lang:tr since:2025-01-08 until:2025-01-09',
        '. lang:tr since:2025-01-13 until:2025-01-14',]

dates3 =['. lang:tr since:2024-11-20 until:2024-11-21',
        '. lang:tr since:2024-11-25 until:2024-11-26',
        '. lang:tr since:2024-12-04 until:2024-12-05',
        '. lang:tr since:2024-12-12 until:2024-12-13',
        '. lang:tr since:2024-12-18 until:2024-12-19',
        '. lang:tr since:2024-12-26 until:2024-12-27',
        '. lang:tr since:2024-12-30 until:2024-12-31',
        '. lang:tr since:2025-01-08 until:2025-01-09',
        '. lang:tr since:2025-01-13 until:2025-01-14',
        '. lang:tr since:2025-01-24 until:2025-01-25',
        '. lang:tr since:2025-01-28 until:2025-01-29',
        '. lang:tr since:2025-02-06 until:2025-02-07',
        '. lang:tr since:2025-02-10 until:2025-02-11']

dates4 =['. lang:tr since:2025-02-20 until:2025-02-21',
        '. lang:tr since:2025-02-27 until:2025-02-28',
        '. lang:tr since:2025-03-05 until:2025-03-06',
        '. lang:tr since:2025-03-11 until:2025-03-12',
        '. lang:tr since:2025-03-20 until:2025-03-21',
        '. lang:tr since:2025-03-26 until:2025-03-27',
        '. lang:tr since:2025-04-01 until:2025-04-02',
        '. lang:tr since:2025-04-10 until:2025-04-11',
        '. lang:tr since:2025-04-16 until:2025-04-17',
        '. lang:tr since:2025-04-23 until:2025-04-24',
        '. lang:tr since:2025-04-30 until:2025-05-01',
        '. lang:tr since:2025-05-08 until:2025-05-09',
        '. lang:tr since:2025-05-13 until:2025-05-14']

bayram_tarihleri = [
#  ". lang:tr since:2024-06-16 until:2024-06-17",  # Kurban Bayramı 1. Gün
#  ". lang:tr since:2024-06-17 until:2024-06-18",  # Kurban Bayramı 2. Gün
#  ". lang:tr since:2024-06-18 until:2024-06-19",  # Kurban Bayramı 3. Gün
#  ". lang:tr since:2024-06-19 until:2024-06-20",  # Kurban Bayramı 4. Gün

    ". lang:tr since:2025-03-30 until:2025-03-31",  # Ramazan Bayramı 1. Gün
    ". lang:tr since:2025-03-31 until:2025-04-01",  # Ramazan Bayramı 2. Gün
    ". lang:tr since:2025-04-01 until:2025-04-02",  # Ramazan Bayramı 3. Gün

#    ". lang:tr since:2024-05-19 until:2024-05-20",  # 19 Mayıs - Atatürk'ü Anma, Gençlik ve Spor Bayramı
#    ". lang:tr since:2024-07-15 until:2024-07-16",  # 15 Temmuz - Milli Birlik ve Demokrasi Günü
#    ". lang:tr since:2024-08-30 until:2024-08-31",  # 30 Ağustos - Zafer Bayramı
#    ". lang:tr since:2024-10-29 until:2024-10-30",  # 29 Ekim - Cumhuriyet Bayramı
#    ". lang:tr since:2025-04-23 until:2025-04-24",  # 23 Nisan - Ulusal Egemenlik ve Çocuk Bayramı
#    ". lang:tr since:2025-05-01 until:2025-05-02",  # 1 Mayıs - Emek ve Dayanışma Günü
]
async def main():
    cookies_path = 'cookies.json'

    async def login_with_cookies():
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

    async def search_tweets(query):
        retries = 0
        max_retries = 5
        while retries < max_retries:
            try:
                tweets = await client.search_tweet(query, 'Top')
                if len(tweets) > 0:
                    print("tweet bulundu")
                for tweet in tweets:
                    tweet_data.append(
                        {'id': tweet.id, 'name': tweet.user.name, 'screen_name': tweet.user.screen_name, 'Date': tweet.created_at,
                         'Text': tweet.text, 'Hashtags': tweet.hashtags, 'Views': tweet.view_count, 'Likes': tweet.favorite_count,
                         'Retweets': tweet.retweet_count, 'Replies': tweet.reply_count, "type": 'gunluk'})
                break  # Success, exit retry loop
            except Exception as e:
                if hasattr(e, '__module__') and 'twikit.errors' in e.__module__ and getattr(e, 'status', None) == 404:
                    retries += 1
                    print(f"twikit.errors.NotFound: status: 404, message: '' - retrying {retries}/{max_retries}")
                    await asyncio.sleep(2)  # Wait 2 seconds before retrying
                else:
                    raise

    #await search_tweets(". lang:tr since:2024-05-20 until:2024-05-21")

    start_date = datetime.strptime("2024-05-17", "%Y-%m-%d")
    end_date = datetime.strptime("2025-05-17", "%Y-%m-%d")

    count = 0
    current_date = start_date + timedelta(days=count)

    await login_with_cookies()

    while current_date <= end_date:
        next_date = current_date + timedelta(days=1)
        await search_tweets(f". lang:tr since:{current_date.strftime('%Y-%m-%d')} until:{next_date.strftime('%Y-%m-%d')}")
        current_date = next_date
        count += 1

        if count % 40 == 0:
            beklemeden_evvelkiler = pd.DataFrame.from_records(tweet_data)
            beklemeden_evvelkiler.to_excel(f'{count}inci twit.xlsx', index=False)
            print("Bekleniyor: 15 dakika...")
            time.sleep(900)  # 15 dakika = 900 saniye
            await login_with_cookies()

    df = pd.DataFrame.from_records(tweet_data)
    df.to_excel('Bir Yıllık.xlsx', index=False)


asyncio.run(main())

