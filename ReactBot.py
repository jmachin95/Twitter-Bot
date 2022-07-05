import tweepy
import time

#You could store this information elsewhere and gather it from another file
api_key = "*Your Key*"
api_secret_key = "*Your Key*"
access_token = "*Your Token*"
access_secret_token = "*Your Token*"

auth = tweepy.OAuthHandler(api_key,api_secret_key)
auth.set_access_token(access_token,access_secret_token)

api = tweepy.API(auth)

try:
     api.verify_credentials()
except Exception as error:
     print(error)


while True: #Another option here would be to use 'track'
    for tweet in tweepy.Cursor(api.search_tweets, q='ReactJs'or'reactjs'or'ReactJS'or'javascript'or'JavaScript').items(10):
        try:
            print('\nRetweet Bot found tweet by @' + tweet.user.screen_name + '. ' + 'Attempting to retweet.')


            api.create_favorite(tweet.id)
            print('Tweet Liked Successfully.')
            tweet.retweet()
            print('Retweet Published Successfully.')
            
            
    

        #This handles the errors and prints it out so that the program can continue even if an error occurs
        except Exception as err:
            print('\nError. Something Went Wrong.')
            print(err)

        #Twitter has automation rules so make sure the 'time.sleep()' value isn't too low     
        time.sleep(10)   

