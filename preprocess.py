# Main imports.
import string
import json
import nltk

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

def filterSentence(sentence, verbose = False):
    ''' 
    Filters sentences from tweets and queries.

    :param str sentence: Documents that are read one by one from the collection
    :param boolean verbose: [Optional] Provide printed output of tokens for testing.
    :return: Tokens to be added to the index (vocabulary)
    :rtype: list
    '''
    # Custom Stopwords that are NOT defined in Library or Provided Stopwords
    edge_stopwords = ['n\'t', '\'d', 'http', 'https']

    # Build a final list of stopwords
    custom_stopwords = set(stopwords.words('english')).union((line.strip('\r\n') for line in open('./assets/stop_words.txt', 'r'))).union(edge_stopwords)

    # Create tokens
    tokens = [ps.stem(word.lower()) for word in word_tokenize(sentence)
        if word.lower() not in custom_stopwords and
            word not in string.punctuation and
            not isNumeric(word)]

    if verbose:
        print()
        print('\t' + '[%s]' % ', '.join(map(str, tokens)) + '\n')

    return tokens

def buildIndex(tokens, verbose = False):
    ''' 
    Filters sentences from tweets and queries.

    :param str tokens: Tokens obtained from the preprocessing module
    :param boolean verbose: [Optional] Provide printed output of tokens for testing.
    :return: An inverted index for fast access
    :rtype: dict
    '''
    # Initialize dictionary and Document id
    dict = {}
    doc_index = 1

    for token in tokens:
        for word in token:
            if word not in dict:
                dict[word] = []
            if word in dict and doc_index not in dict[word]: 
                dict[word].append(doc_index)
        
        doc_index += 1

    if verbose:
        print ('\r Dictonary:')
        print (json.dumps(dict, indent = 2))
        print ('-' * 40)

    return dict