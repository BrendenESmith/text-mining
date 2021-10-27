import tweepy
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# sentence = "Dune's visuals were so stunning"
# score = SentimentIntensityAnalyzer().polarity_scores(sentence)
# print(score)


# Keys and secrets
TOKEN = '1049810324365430786-L0iaMkrCz1uNxygUycZFdFhExC4ULT'
TOKEN_SECRET = 'vmoBdQ9Q96LEif5hIxyOVao3KQgO4ZSROs9bMbnprthK1'
CONSUMER_KEY = 'mZ5gp1MWCi0aEmecoUxvWUEO3'
CONSUMER_SECRET = 'YhwtTjvEe1zPnlUSlCWOVFRJsWXE8jgo4ek4pHaHJPqPHpRsst'

BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAKObVAEAAAAASmYKqe7QJEqJpHRcDgvGSmKnSqI%3DQsdD34IKqTbqfmjcnTuzrqTzZbkzoF8VsropQqjGj0BoqEEPYh"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(TOKEN,TOKEN_SECRET)

api = tweepy.API(auth)

# for tweet in api.search_tweets(q="Dune", lang="en", count = 5):
#     print(f"{tweet.user.name}: {tweet.text}")

tweet_counter = 0
total_compound = 0
for tweet in api.search_30_day(label = "30DaySearch", query = "Biden", maxResults = 100):
    if "RT" not in tweet.text:
        print(f"{tweet.user.name} at {tweet.created_at}: {tweet.text}")
        score = SentimentIntensityAnalyzer().polarity_scores(tweet.text)
        compound = score["compound"]
        total_compound = total_compound + compound
        print(f"Sentiment Score: {score}")
        print()
        tweet_counter += 1
        if tweet_counter >= 10:
            break

print(f"Total compound score: {total_compound}; Average compound score: {(total_compound/10)}")