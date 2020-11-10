"""
This file is used to analyse the sentiments of a tweet
based on dataset of collection of words we have.

References:
- https://numpy.org/doc/1.19/user/quickstart.html
"""

# import libraries
from dataclasses import dataclass
from typing import List, Dict
from datetime import datetime
import csv
import ast


@dataclass
class Tweet:
    """
    Tweet datatype represents a tweet in the dataset we have
    with all its information.

    Instance Attributes:
    - text: text of the tweet
    - hashtags: list of hashtags in mentioned in the tweet
    - likes: number of likes on the tweet
    - retweet: the number of times the tweet was retweeted
    - timestamp: date and time when the tweet was posted
    - username: username of the person who posted the tweet
    - followers: number of followers the user has
    - location: user's location

    Representation Invariants:
      - self.likes >= 0
      - self.retweets >= 0
      - self.followers >= 0
    """
    text: str
    hashtags: List[Dict]
    likes: int
    retweets: int
    timestamp: datetime
    username: str
    followers: int
    location: str


def extract_tweeter_data(filename: str) -> List[Tweet]:
    """ The function reads the dataset with all the tweets and convert each tweet
    in the data into a Tweeter object to store the sata.

    @param filename: the path of the dataset with all the tweets
    @return: a list of Twitter objects

    Preconditions:
    - filename is a valid path
    """

    # extracting the tweet text out of the data
    with open(filename) as file:
        reader = csv.reader(file)

        next(reader)

        reader = list(reader)

        data = [Tweet(row[0],
                      ast.literal_eval(row[1]),
                      int(row[2]),
                      int(row[3]),
                      datetime.fromisoformat(row[4]),
                      row[5],
                      int(row[6]),
                      row[7]) for row in reader]

        return data


def extract_words(filename: str) -> List[Dict[str, float]]:
    """ The function reads the dataset with all the positive and negative words
    and returns a list of dicts with all the words mapped to a score of -1 to 1
    where -1 is very negative and 1 is very positive word. if a word has a score
    of 0 then the word is neutral.

    The words in the data are in the form of lemma, that is word#type where type
    can be adjectives, nouns, verbs and adverbs. we will remove the type and only
    keep the word.

    Also words have _ and - instead of space, but while writing tweets we usually
    do not use - or _, instead we us space, thus we would replace all - and _ to
    space.

    @param filename: the path of the dataset with all the words and their cores
    @return: a list of dicts mapping word to its score

    Preconditions:
    - filename is a valid path
    """

    # extracting the file
    with open(filename) as file:
        reader = [line for line in file.read().split('\n') if line != '' and line[0] != '#']

        words_so_far = []  # ACCUMULATOR: stores the return data

        for line in reader:
            lemma, pos = line.split()

            word = lemma.split('#')[0].replace('-', ' ').replace('_', ' ')  # modifying the word
            score = float(pos)  # converting score into numeric data type

            words_so_far.append({word: score})  # adding word and its score to return list

        return words_so_far





