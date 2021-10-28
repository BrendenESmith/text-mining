import tweepy
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import statistics


def tweet_sentiments(topic, num_of_tweets):
    """This function takes a user-entered topic and how many tweets they'd like to see and prints out those tweeets,
    an accompanying sentiment scores, and then computes several summary statistics on the sentiments of the tweets."""
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
    tweet_list_compounds = []
    for tweet in api.search_30_day(label = "30DaySearch", query = topic, maxResults = 100):
        if "RT" not in tweet.text:
            score = SentimentIntensityAnalyzer().polarity_scores(tweet.text)
            overall_compound = score["compound"]
            if overall_compound != 0.0:
                print(f"{tweet.user.name} at {tweet.created_at}: {tweet.text}")
                compound = score["compound"]
                tweet_list_compounds.append(compound)
                print(f"Sentiment Score: {score}")
                print()
                tweet_counter += 1
                if tweet_counter >= num_of_tweets:
                    break

    # Learned of statistics package on Slack overflow
    print(tweet_list_compounds)
    total_compound = sum(tweet_list_compounds)
    avg_compound_score = statistics.mean(tweet_list_compounds)
    abs_compounds = [abs(x) for x in tweet_list_compounds]
    total_abs_compound = sum(abs_compounds)
    avg_abs_compound_score = statistics.mean(abs_compounds)
    standard_deviation = statistics.stdev(tweet_list_compounds)

    print(f"Total compound score: {total_compound}; Average compound score: {avg_compound_score}")
    print(f"Total absolute compound score: {total_abs_compound}; Average absolute compound score: {avg_abs_compound_score}")
    print(f"Standard deviation: {standard_deviation}")

# tweet_sentiments("pizza", 50)


def tweet_grammar(handle, no_of_tweets):
    """"""
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

    grammar_dict = dict()
    for tweet in api.user_timeline(screen_name = handle, count = no_of_tweets, include_rts = False):
        print(tweet.text)
        text = nltk.word_tokenize(tweet.text)
        grammar_list = (nltk.pos_tag(text))
        for tup in grammar_list:
            if tup[1] not in grammar_dict:
                grammar_dict[tup[1]] = 1
            else:
                grammar_dict[tup[1]] += 1
        print(sorted(grammar_dict.items(), key = lambda item: item[1], reverse = True))
        print()

tweet_grammar("POTUS", 5)
