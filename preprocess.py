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
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('stem.porter')

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
    # Initialize dictionary containing the frequency of the word from all the tokens.
    word_occurences_all_tokens = dict()
    # Initialize dictionary containing the frequency of the word per token for all Tokens.
    word_occurences_per_token = dict()
    # Initialize dictionary containing the idf calcution for all the words in all Tokens.
    word_idf = dict()
    # Use document ID instead of this counter
    doc_index = 1
    for document in documents:
        # Initialize temporary dictionary used to store the frequency of the words per Document.
        word_frequency = dict()
        for token in document:
            if token not in word_frequency:
                word_frequency[token] = 1
            else:
                word_frequency[token] += 1

            if token not in word_occurences_all_tokens:
                word_occurences_all_tokens[token] = 1
            else:
                word_occurences_all_tokens[token] += 1
        word_occurences_per_token[doc_index] = word_frequency
        doc_index += 1
    
    # Calulating the idf for all words in all Document.
    for word in word_occurences_all_tokens:
        word_idf[word]= round(math.log((len(documents) / word_occurences_all_tokens[word]), 2), 3)

    # Calculating the tf-idf for the words within the Documents
    for index, doc in word_occurences_per_token.items():
        for token in doc:
            # tf-idf = tf * idf
            doc[token] = doc[token] * word_idf[token]

    # {doc_id: {token : {idf: 0.585, }}}
    print("Word occurences per token", word_occurences_per_token)
    print("word idf", word_idf)

    return

def step3(query, ):
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
        # tf-idf = (0.5 + 0.5*tf_iq) * idf_i
        query_word_occurences[word] = (0.5 + (0.5 * query_word_occurences[word])) * word_idf[word]
        print("query word",word,"tf-idf",query_word_occurences[word])

    # Calculating the lenghts for all document
    doc_lenght_counter = 1
    for index, doc in word_occurences_per_token.items():
        tmp_length = 0
        for word in doc:
            tmp_length += pow(doc[word],2)
        length_per_token[doc_lenght_counter] = round(math.sqrt(tmp_length),3)
        doc_lenght_counter +=1
    print(length_per_token)

    # QUERY WORK FOR STEP 3
    # Calculating the lenghts for the query
    tmp_query_length = 0
    for word in query_word_occurences:
        print(query_word_occurences[word])
        tmp_query_length += pow(query_word_occurences[word],2)
    length_of_query = round(math.sqrt(tmp_query_length),3)
    print("Query length:",length_of_query)
    # print(word_occurences_per_token)
    sim = dict()
    tmp_dict = 1
    for index, doc in word_occurences_per_token.items():
        tmp_sim = 1
        for word in doc:
            if(word in query_word_occurences):
                tmp_sim += doc[word] * query_word_occurences[word]
                # print("query",word,query_word_occurences[word])
                # print(word,doc[word])
        
        magnitude = length_per_token[tmp_dict]*length_of_query
        dotProduct = float(tmp_sim)

        try:
            sim[tmp_dict] = dotProduct/magnitude
        except:
            print("Magnitude is",magnitude)

        # sim["D"+str(tmp_dict)+"cosSim"] = tmp_sim / x
        # print("Numerator", tmp_sim)
        #print(sim["D"+str(tmp_dict)+"cosSim"])
        # print('Denom',length_per_token["DL"+str(tmp_dict)]*length_of_query)
        # print(sim["D"+str(tmp_dict)+"cosSim"])
        tmp_dict+=1

    if verbose:
        print ('\r Dictonary:')
        print (json.dumps(dict_words, indent = 2))
        print ('-' * 40)

    return tokens