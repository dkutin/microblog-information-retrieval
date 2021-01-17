# Main imports.
import string
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

    :param str sentence: The sentence to be tokenized with stopwords and punctuation removed.
    :param boolean verbose: [Optional] Provide printed output of tokens for testing.
    :return: the tokenized sentence.
    :rtype: string
    '''
    custom_stopwords = set(stopwords.words('english')).union((line.strip('\r\n') for line in open('./assets/stop_words.txt', 'r')))

    tokens = [ps.stem(word.lower()) for word in word_tokenize(sentence)
        if not word in custom_stopwords and 
            not word in string.punctuation and
            not isNumeric(word)]

    if verbose:
        print (tokens)

    return tokens