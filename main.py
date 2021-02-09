# Import helper functions
from preprocess import importQuery, importTweets, buildIndex, lengthOfDocument
from results import retrieve

def main():
    print("\n CSI 4107 - Microblog information retrieval system \n")

    # Load the tweet list.
    # {'34952194402811904': 'Save BBC World Service from Savage Cuts http://www.petitionbuzz.com/petitions/savews', ...}
    tweets = importTweets(True)

    # Load the list of queries.
    # {1: ['bbc', 'world', 'servic', 'staff', 'cut'], ...}
    queryFile = importQuery(True)

    # Build the inverted index.
    index = buildIndex(tweets, True)

    length = lengthOfDocument(index, tweets)

    print(length)

    # Rank all queries
    print(retrieve(queryFile, index))

    # Load the query list.

    #Finding and ranking the documents of the query
    # result = rankingQuery(queryFile, True)
    # print(result)

if __name__ == "__main__":
    main()
