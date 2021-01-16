# Main imports.
import string
import nltk

# Import specific packages.
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download packages if not installed locally.
nltk.download('stopwords')
nltk.download('punkt')

def filterSentence(sentence):
    ''' 
    Filters sentences from tweets and queries.

    :param str sentence: The sentence to be tokenized with stopwords and punctuation removed.
    :return: the tokenized sentence.
    :rtype: string
    '''
    custom_stopwords = set(stopwords.words('english')).union((line.strip('\r\n') for line in open('./assets/stop_words.txt', 'r')))

    tokens = [word.lower() for word in word_tokenize(sentence)
        if not word in custom_stopwords and not word in string.punctuation]

    return tokens

# Example test case, will still have to load the data.
for word in filterSentence("""I'd very much appreciate it if people would stop broadcasting asking me to add people on BBM."""):
    print (word)