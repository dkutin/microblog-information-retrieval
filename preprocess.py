# Main imports.
import string
import json
import nltk
import math

# Import specific packages.
from nltk.corpus import stopwords
from nltk.corpus.reader.panlex_lite import Meaning
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

    :param str sentence: The sentence to be tokenized with stopwords and punctuation removed.
    :param boolean verbose: [Optional] Provide printed output of tokens for testing.
    :return: the tokenized sentence.
    :rtype: list
    '''
    tweet_list = dict()
    # Splits tweet list at newline character.
    tweets = (line.strip('\n') for line in open('./assets/tweet_list.txt', 'r', encoding='utf-8-sig'))

    # Build the dictionary.
    for tweet in tweets:
        key, value = tweet.split('\t')
        # Tokenize each tweet, and put back in list.
        tweet_list[key] = filterSentence(value, verbose)

    return tweet_list

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
    global inverted_index      #declared the inverted_index to be global in order for the ranking query to have access
    inverted_index = dict()

    # Initialize dictionary containing the idf calcution for all the words in all Tokens.
    global word_idf        #declared the word_idf to be global as well
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



def rankingQuery(query, verbose = False):
    '''
    Step 3: Filters sentences from tweets and queries.

    :param list documents: Documents obtained from the preprocessing module
    :param boolean verbose: [Optional] Provide printed output of tokens for testing.
    :return: the lengths for the tokens
    :rtype: dict
    '''
    # Initialize length of query.
    length_of_query = 0
    # Initialize dictionary containing the lenths of all the Tokens.
    length_per_token = dict()
    # Initialize dictionary containing the frequency of the word in query.
    query_word_occurences = dict()
    
    # QUERY WORK FOR STEP 3

    # Calculating the tf-idf for the words within the Query
    for word in query:
        if word not in query_word_occurences:
                query_word_occurences[word] = 1
        else:
            query_word_occurences[word] += 1

    for word in query_word_occurences:
        # Formular given: tf-idf = (0.5 + 0.5*tf_iq) * idf_i

        query_word_occurences[word] = (0.5 + (0.5 * query_word_occurences[word])) * word_idf[word]
        print("Query Word: {} and Tf-Idf: {}".format(word, query_word_occurences[word]))


    # Calculating the lenghts for all document
    doc_lenght_counter = 1
    for index, doc in inverted_index.items():
        tmp_length = 0
        for word in doc:
            tmp_length += pow(doc[word],2)
        length_per_token[doc_lenght_counter] = round(math.sqrt(tmp_length),3)
        doc_lenght_counter +=1
    print("Token length:", length_per_token)

    # Calculating the lenghts for the query
    tmp_query_length = 0
    for word in query_word_occurences:
        # print(query_word_occurences[word])
        tmp_query_length += pow(query_word_occurences[word],2)
    length_of_query = round(math.sqrt(tmp_query_length),3)
    print("Query length:",length_of_query)
    
    
    sim = dict()
    tmp_dict = 1
    for index, doc in inverted_index.items():
        tmp_sim = 1
        for word in doc:
            if(word in query_word_occurences):
                tmp_sim += doc[word] * query_word_occurences[word]

        
        magnitude = length_per_token[tmp_dict]*length_of_query
        dotProduct = float(tmp_sim)

        try:
            sim[tmp_dict] = dotProduct/magnitude
        except:
            print("Magnitude is",magnitude)

        tmp_dict+=1

    if verbose:
        print ('\r Dictonary:')
        print (json.dumps(query_word_occurences, indent = 2))
        print ('-' * 40)

    return length_per_token

