"""
This file is used to extract data from the twitter api and
make the dataset we would work on to make conclusions and
analyze real world statistics.

References:
- https://www.programiz.com/python-programming/writing-csv-files
- https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/overview/tweet-object
- http://docs.tweepy.org/en/v3.5.0/cursor_tutorial.html
- http://docs.tweepy.org/en/v3.5.0/api.html#tweepy-api-twitter-api-wrapper
"""


import tweepy  # for getting tweets
import csv  # for storing the data
from typing import List  # for better annotation

"""keys required to authenticate that we are valid users
these are provided by twitter API, when we create a project/App"""

keys = {'consumer_key': 'oYpwnrbV5Y9ALcdwdQhRkSsLR',
        'consumer_key_secret': 'HHF5PMHys5oFfUeqFgKJIZRwkq0vyWl0mKyBaU3zIFyAV2GCMO',
        'Access_token': '1323930219263135745-exoYkKfak1aosBU0eVDWTzxW1AFAjo',
        'Access_token_secret': 'ilX1qD8VROXJh9CG7ow5OPJG2wnPXxpmuWTlXYAAHAyVF'}

tags = ['#climatechange',
        '#climatechangeisreal',
        '#actonclimate',
        '#globalwarming',
        '#climatechangehoax',
        '#climatedeniers',
        '#climatechangeisfalse',
        '#globalwarminghoax',
        '#climatechangenotreal']


def get_tags(hashtags: List[str]) -> List[str]:
    """Return a list of all the hashtags in the string

    >>> get_tags(['#climatechange', '#climatechangeisreal'])
    ['climatechange', 'climatechangeisreal']
    """

    return [word[1:] for word in hashtags]


def search_for_query(consumer_key: str, consumer_key_secret: str, access_token: str, access_token_secret: str,
                     hashtags: List[str], items: int) -> None:
    """
    This function will get us the most recant <items> tweets on the hashtags we give the function in the form of
    a search query. Here we use the tweepy api to extract these tweets and write all these tweets on csv. We can
    extract many features out of the tweets like the its timestamp,the tweet, username, all the hashtags in that
    tweet, followers count of that user, location if mentioned and many more, but we would only extract a few of
    them.

    @param consumer_key: A unique key for our project/app assigned by twitter for authentication
    @param consumer_key_secret: A unique key for our project/app assigned by twitter for authentication
    @param access_token: A unique key for our project/app assigned by twitter for authentication
    @param access_token_secret: A unique key for our project/app assigned by twitter for authentication
    @param hashtags: A list of strings containing all the hashtags for which we want to get tweets
    @param items: The number of tweets we want from the most latest tweet
    @return: None

    Preconditions:
    - consumer_key is a valid twitter consumer key
    - consumer_key_secret is a valid twitter secret consumer key
    - access_token is a valid twitter access token
    - access_token_secret is a valid twitter secret access token
    - items > 0
    """

    # using tweepy to authenticate for accessing twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    # initializing API used to do access all the function in the library
    api = tweepy.API(auth)

    # creating the file to store data in
    filename = '_'.join(get_tags(hashtags)) + '.csv'

    with open(filename, 'w', newline='') as file:
        write = csv.writer(file)

        # add column names, as the first row of the dataset we would create
        # these are all the features we would extract from the tweets
        write.writerow(
            ['tweet_text',  # text of the tweet
             'all_hashtags',  # list of all the hashtags in the tweet
             'favorite_count',  # number of likes to the tweet
             'retweet_count',  # number of times the tweet was retweeted
             'created_at',  # date and time of creation
             'username',  # username of the person who tweeted the tweet
             'followers_count',  # number of followers the user has
             'location'])  # the location of the user

        # request the data the twitter api

        # we would be using api.search function to get the tweets which takes in parameters like the search query,
        # page from which we want to extract (1 <= page <= 1500). A single page has only about 100 tweets and if we
        # want more tweets we have to call the function multiple times on different pages. Thus we would use
        # "tweppy.Coursor" function in which we could specify the number of tweets we want and it would automatically
        # change the page.

        # defining attribute values
        search_query = ' AND '.join(hashtags) + ' -filter:retweets'  # here '-filter:retweets' would filter out retweets
        language = 'en'  # the language we want our tweets to be in
        mode = 'extended'  # mode tells us if we want only the default feature or more feature of a tweet

        # extracting tweets in a list.
        # tweets here is a list of tweet objects which contains all the information about a tweet
        tweets = tweepy.Cursor(api.search, q=search_query, lang=language, tweet_mode=mode).items(items)

        # extracting out the features we want from the tweets and writing them into csv file
        for tweet in tweets:
            write.writerow([
                tweet.full_text.replace('\n', ' '),  # the text of the tweet in one line rather than multiple lines
                tweet.entities.get('hashtags'),  # list of dicts where each dict contains info about a sing hashtag
                tweet.favorite_count,  # number of likes on the tweet
                tweet.retweet_count,  # number of times this tweet has been retweeted
                tweet.created_at,  # the date and time of creation
                tweet.user.screen_name,  # username of the user
                tweet.user.followers_count,  # number of followers the user has
                tweet.user.location  # location of the user
            ])


if __name__ == '__main__':
    items_per_tag = 2

    for tag in tags:
        search_for_query(keys['consumer_key'],
                         keys['consumer_key_secret'],
                         keys['Access_token'],
                         keys['Access_token_secret'],
                         [tag],
                         items_per_tag)

