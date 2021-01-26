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

def filterSentence(sentence, verbose = False):
    ''' 
    Step 1: Filters sentences from tweets and queries.

    :param str sentence: The sentence to be tokenized with stopwords and punctuation removed.
    :param boolean verbose: [Optional] Provide printed output of tokens for testing.
    :return: the tokenized sentence.
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

    # Initialize dictionary containing the idf calcution for all the words in all Tokens.
    word_idf = dict()

    # Use document ID instead of this counter
    doc_index = 1
    for document in documents:
        # Initialize temporary dictionary used to store the frequency of the words per Document.
        for token in document:
            if token not in inverted_index:
                inverted_index[token] = {}
            if token in inverted_index and doc_index not in inverted_index[token]:
                inverted_index[token][doc_index] = 1
            elif doc_index in inverted_index[token]:
                inverted_index[token][doc_index] += 1

        doc_index += 1

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
