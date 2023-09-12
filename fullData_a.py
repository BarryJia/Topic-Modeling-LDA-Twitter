import tweepy
import json
import math
import glob
import csv
import zipfile
import zlib
from tweepy import TweepError
from time import sleep
import _locale
import random
_locale._getdefaultlocale = (lambda *args: ['en_US', 'utf8'])

user = 'covid'
def getContent(fileBefore):
    user = 'covid'
    # fileBefore = 'data/after/0201'

    with open('api_keys.json') as f:
        keys = json.load(f)

    auth = tweepy.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
    auth.set_access_token(keys['access_token'], keys['access_token_secret'])
    api = tweepy.API(auth)
    user = user.lower()
    output_file = '{}.json'.format(user)
    output_file_short = '{}_short.json'.format(user)
    compression = zipfile.ZIP_DEFLATED
    print("next step: open "+fileBefore+".json")
    # with open('dataset.json') as f:
    #     tweets = json.load(f)
    tweets = []
    tweetsPro = []
    count = 0
    for line in open(fileBefore+'t1.json', 'r'):
        # tweetsPro.append(json.loads(line))
        tweets.append(json.loads(line))
        # if (count%3 == 0):
        #     tweetsPro.append(json.loads(line))
        count += 1
    # tweets = random.sample(tweetsPro, 50000)
    print("success in opening file: "+fileBefore+".json")
    ids = []
    for tweet in tweets:
        ids.append(tweet['tweet_id'])

    print('total ids: {}'.format(len(ids)))
    print('pre-operated total ids: {}'.format(count))

    all_data = []
    unitNum = 100
    start = 0
    end = start+unitNum
    limit = len(ids)
    i = math.ceil(limit / unitNum)
    tmp=[]
    csvFile = open(fileBefore+'_full.csv', 'a',encoding='utf-8',newline='')
    csvWriter = csv.writer(csvFile)
    for go in range(i):
        try:
            print('currently getting {} - {}'.format(start, end))
            sleep(1)  # needed to prevent hitting API rate limit
            id_batch = ids[start:end]
            start += unitNum
            end += unitNum
            tweets = api.statuses_lookup(id_batch)
            for status in tweets:
                    csvWriter.writerow([status.id, status.text])
        except BaseException as e:
            print('failed on_status, ',str(e))
            start -= unitNum
            end -= unitNum
            sleep(30)

if __name__=="__main__":
    # for num in range(18,31):
    #     if (num < 10):
    #         getContent("data/after/040" + str(num))
    #         sleep(60)
    #     else:
    #         getContent("data/after/04"+str(num))
    #         sleep(60)
    # getContent("data/after/0229"+str(num))
    getContent("data/after/0501")
    print("Finished")
