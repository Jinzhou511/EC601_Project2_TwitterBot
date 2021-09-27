import tweepy
import time
key='API KEY'
secret='API SECRET'
consumer_key='ACCESS KEY'
consumer_secret='ACCESS SECRET'
key='1393886621729271815-MSUMYiX5E7dOqv688WtlRDL861LVEg'
secret='kRPXGNrEecnKUTg1n0Xm4nxFQ22loyuoKkFdbjzSYdskM'
consumer_key='JR6B8K1QWpYeMqMKYAiGkIF3l'
consumer_secret='A83zp1kFCtrBTNmpwNnxXWRLRTsSshmRkRkl9MV29Bu7DYkBZm'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)
#send a tweet
#api.update_status('I just relpy an accout')

FILE_NAME = 'last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME,'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write=open(FILE_NAME,'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

#tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
def reply():

    print(read_last_seen(FILE_NAME))
    #print(tweet_mode='extended')
    tweets = api.mentions_timeline(1442165160123277319,tweet_mode='extended')
    for tweet in reversed(tweets):
        if '#zjz' in tweet.full_text.lower():
            print(str(tweet.id)+'-'+tweet.full_text)
            api.update_status("@"+tweet.user.screen_name+"auto reply is now working",tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)  
            store_last_seen(FILE_NAME,tweet.id)


while True:
    reply()
    time.sleep(60)