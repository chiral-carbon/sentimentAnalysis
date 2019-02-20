import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

class TwitterClient(object):

	def __init__(self):
		#Enter data from your Twitter Developer account
		consumer_key = 
		consumer_secret = 
		access_token = 
		access_token_secret = 

		self.auth = OAuthHandler(consumer_key, consumer_secret)
		self.auth.set_access_token(access_token, access_token_secret)
		self.api = tweepy.API(self.auth)

	def sentiment(self, tweet):
		formatted = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
		analysis = TextBlob(self.formatted)

		if analysis.sentiment.polarity > 0:
			return 'positive'
		elif analysis.sentiment.polarity == 0:
			return 'neutral'
		else:
			return 'negative'

	def compute(self, query, count=10):
		tweets= []
		fetched_tweets = self.api.search(q = query, count = count)

		for tweet in fetched_tweets:
			parsed_tweet = {}

			parsed_tweet['text'] = tweet.text
			parsed_tweet['sentiment'] = self.sentiment(tweet.text)

			if tweet.retweet_count > 0:
				if parsed_tweet not in tweets:
					tweets.append(parsed_tweet)

				else:
					tweets.append(parsed_tweet)
			
		return tweets


if __name__ == '__main__':
	api = TwitterClient()
	myQuery = input("Enter a query to find the sentiment on Twitter regarding it: ")
	
	tweets = api.compute(query = myQuery, count = 200)

	ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
	print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))

	ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
	print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
		
	print("Neutral tweets percentage: {} %".format(100*(len(tweets) - len(ptweets)- len(ntweets))/len(tweets)))

	print("\n\nPositive tweets:")
	for tweet in ptweets[:10]:
		print(tweet['text'])

	print("\n\nNegative tweets:")
	for tweet in ntweets[:10]:
		print(tweet['text'])



		
