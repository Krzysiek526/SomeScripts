# install 'pip3 install tweepy' in folder

import tweepy
import time

auth = tweepy.OAuthHandler('YLmgdzxIfbtryNFqQYR9Slxq5',
                           'J9uDwjfucqauFhnTe4hnRkKOaexVbbTh7DDU1pw379FWvcWUKG')
auth.set_access_token('999370399174615041-O5cqnwjs4hJpcMfNWOL5Is3Ob938ikl',
                      '0yIjTPLVzBIi11mI0LfotXUqoilfUnymD4IA5PB5ChIT3')

api = tweepy.API(auth)

# printing tweets from timeline in command line
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)


user = api.me()

# prints information about me
# print(user.name)
# print(user.screen_name)


#########################
# Tweet Bot

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)


# looking for tweets containig the words python
search_string = 'python'
numbersofTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numbersofTweets):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

# # Genrous Bot - adding followers to followed
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     #print(follower.name)
#     if follower.name == 'john': #name from followers
#         follower.follow()
#         break
        # if follower.followers_count >100:
        #     follower.follow()
        #     break
