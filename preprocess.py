import string

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Not sure how to add these yet, 
# had to do it through `python3`
################################
# nltk.download('stopwords')
# nltk.download('punkt)

# This filters tweets and queries.
def filterSentence(sentence):
    custom_stopwords = set(stopwords.words('english')).union((line.strip('\r\n') for line in open('./assets/stopwords.txt', 'r')))

    tokens = [word.lower() for word in word_tokenize(sentence) 
        if not word in custom_stopwords and not word in string.punctuation]

    return tokens

for word in filterSentence("""I'd very much appreciate it if people would stop broadcasting asking me to add people on BBM."""):
    print (word)