# Main imports.
import string
import json
import nltk
import math

# Import specific packages.
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer

# Download packages if not installed locally.
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('stem.porter')

# Initialize stemmer
ps = PorterStemmer()

def isNumeric(subj):
    ''' 
    Check if a string contains numerical values.

    :param str subj: the string to be converted
    :return: True if a subject string is a number, False otherwise.
    :rtype: boolean
    '''
    try:
        return float(subj)
    except Exception:
        return False

def importTweets(verbose = False):
    ''' 
    Import tweets from collection.

    :param boolean verbose: [Optional] Provide printed output of tokens for testing.
    :return: the tokenized list of queries.
    :rtype: list
    '''
    tweet_list = dict()
    # Splits tweet list at newline character.
    # tweets = (line.strip('\n') for line in open('./assets/tweet_list.txt', 'r', encoding='utf-8-sig'))
    tweets = (line.strip('\n') for line in open('./assets/tweet_list.txt', 'r', encoding='utf-8-sig'))

    # Build the dictionary.
    for tweet in tweets:
        key, value = tweet.split('\t')
        # Tokenize each tweet, and put back in list.
        tweet_list[key] = filterSentence(value, verbose)

    return tweet_list


def importQuery(verbose = False):
    ''' 
    Import query from collection.

    :param boolean verbose: [Optional] Provide printed output of tokens for testing.
    :return: the tokenized list of queries.
    :rtype: list
    '''
    query_list = dict()

    with open('./assets/test_queries.txt', 'r') as file:
        fileContents = file.read()

    queryCheck = fileContents.strip('\n').split('\n\n')

    current_tweet = 1
    for x in queryCheck:
        save = x[x.index('<title>'): x.index('</title>')].strip('<title> ')
        query_list[current_tweet] = filterSentence(save, verbose)
        current_tweet+=1

    return query_list

def filterSentence(sentence, verbose = False):
    ''' 
    Step 1: Filters sentences from tweets and queries.

    TODO: Filter URLS, Non-english characters, punctuation embedded in words, and unicode characters. 

    :param str sentence: The sentence to be tokenized with stopwords and punctuation removed.
    :param boolean verbose: [Optional] Provide printed output of tokens for testing.
    :return: the tokenized sentence.
    :rtype: list
    '''
    # Custom Stopwords that are NOT defined in Library or Provided Stopwords
    edge_stopwords = ['n\'t', '\'d', 'http', 'https', '//', '...']

    # Build a final list of stopwords
    custom_stopwords = set(stopwords.words('english')).union((line.strip('\r\n') for line in open('./assets/stop_words.txt', 'r'))).union(edge_stopwords)

    # Create tokens
    tokens = [ps.stem(word.lower()) for word in word_tokenize(sentence)
        if word.lower() not in custom_stopwords and
            word not in string.punctuation and
            not isNumeric(word)]

    if verbose:
        print('\n Testing string: \n\n\t ' + sentence + '\n')
        print(' Tokenized:\n')
        print('\t' + '[%s]' % ', '.join(map(str, tokens)) + '\n')

    return tokens

def buildIndex(documents, verbose = False):
    ''' 
    Step 2: Filters sentences from tweets and queries.

    :param list documents: Documents obtained from the preprocessing module
    :param boolean verbose: [Optional] Provide printed output of tokens for testing.
    :return: An inverted index for fast access
    :rtype: dict
    '''
    # Initialize returned index
    inverted_index = dict()

    word_idf = dict()
  
    # Store the frequency of each word in each document.
    for index, document in documents.items():
        for token in document:
            if token not in inverted_index:
                inverted_index[token] = {}
            if token in inverted_index and index not in inverted_index[token]:
                inverted_index[token][index] = 1
            elif index in inverted_index[token]:
                inverted_index[token][index] += 1

    # Calulating the idf for all words in all Document.
    for token, current_document in inverted_index.items():
        total_occurence = 0
        for document, occurence in current_document.items():
            total_occurence += occurence

        word_idf[token] = round(math.log((len(documents) / total_occurence), 2), 3)

    # Calculating the tf-idf for the words within the Documents
    for token, document_info in inverted_index.items():
        for document, occurence in document_info.items():
            document_info[document] = occurence * word_idf[token]

    if verbose:
        print("\r Inverted Index")
        print(json.dumps(inverted_index, indent = 2))
        print("-" * 40)

    return inverted_index

def lengthOfDocument(inverted_index, tweets, verbose = False):
    document_lengths = dict()

    for tweet_id, tweet in tweets.items():
        document_length = 0
        for token in tweet:
            document_length += pow(inverted_index[token][tweet_id], 2)

        document_lengths[tweet_id] = round(math.sqrt(document_length), 3)

    if verbose:
        print('Length of documents', document_lengths)

    return document_lengths
