from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

class TweetStreamListener(StreamListener):
    def on_status(self,status):
        print(status)
        return True

    def on_error(self, status):
        print(status)
        return False

if __name__== "__main__":

	#authorization
    CONSUMER_KEY="lky4UwSu61p4mPnkwKIjHhlU6"
    CONSUMER_SECRET="TV1ycrn39ied2x3hMokqaGgxT9XzFGF9Xr6kLcWoXy62Y6p4By"
    ACCESS_KEY="1095418256553377792-sGTGItL7buu8drVW45JvDGXiByPrs5"
    ACCESS_SECRET="c2vFg2WyotvweMwWZV8J78nvifToqK5XI7iZWf8KZat5n"

    tweetStreamListener = TweetStreamListener()
    authorizeUser = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    authorizeUser.set_access_token(ACCESS_KEY,ACCESS_SECRET)

    stream = Stream(authorizeUser, tweetStreamListener)
	
	#streaming tweets with 'Halifax' keyword
    stream.filter(track=['Halifax'])
	
	python mapreduce.py clean_search_data.py

	python mapreduce.py clean_stream_data.py

    
