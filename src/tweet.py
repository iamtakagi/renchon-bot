import tweepy
from makeSentences import make_sentences
import numpy as np
from twitterApi import api 
from discordWebhook import send
import asyncio

async def tweet():
    loop = asyncio.get_event_loop()
    # 10%の確率で「にゃんぱすー」を呟く
    if np.random.randint(1,91) == 1:
        nyanpass_status = api.update_status(status = "にゃんぱすー")
        nyanpass_link = "https://twitter.com/nyanpassnanon/status/{nyanpass_status.id}"
        send(nyanpass_link)
    sentence_1, sentence_2 = make_sentences()
    tweet_results = loop.run_until_complete(asyncio.gather(
        api.update_status(status = sentence_1),
        api.update_status(status = sentence_2)
    ))
    status_link_1 = f'https://twitter.com/nyanpassnanon/status/{tweet_results[0].id}'
    status_link_2 = f'https://twitter.com/nyanpassnanon/status/{tweet_results[1].id}'
    loop.run_until_complete(asyncio.gather(
        send(status_link_1),
        send(status_link_2)
    ))

