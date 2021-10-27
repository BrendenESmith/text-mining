import tweepy


# Keys and secrets
TOKEN = '1049810324365430786-L0iaMkrCz1uNxygUycZFdFhExC4ULT'
TOKEN_SECRET = 'vmoBdQ9Q96LEif5hIxyOVao3KQgO4ZSROs9bMbnprthK1'
CONSUMER_KEY = 'mZ5gp1MWCi0aEmecoUxvWUEO3'
CONSUMER_SECRET = 'YhwtTjvEe1zPnlUSlCWOVFRJsWXE8jgo4ek4pHaHJPqPHpRsst'

BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAKObVAEAAAAASmYKqe7QJEqJpHRcDgvGSmKnSqI%3DQsdD34IKqTbqfmjcnTuzrqTzZbkzoF8VsropQqjGj0BoqEEPYh"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(CONSUMER_KEY,TOKEN_SECRET)

api = tweepy.API(auth)

for tweet in api.search_tweets(q="covid vaccine", lang="en", rpp = 10):
    print(f"{tweet.user.name}: {tweet.text}")

# for tweet in api.search_30_day(label = "30DaySearch", query = "Dune", maxResults = 10):
#     print(f"{tweet.user.name}: {tweet.text}")