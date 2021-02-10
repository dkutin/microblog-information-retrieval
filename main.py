# Import helper functions
from preprocess import importQuery, importTweets, buildIndex, lengthOfDocument
from results import retrieve
from write import resultFileCreation

def main():
    print("\n CSI 4107 - Microblog information retrieval system \n")

    print("\n Preprocessing... \n")
    # Load the tweet list.
    # {'34952194402811904': 'Save BBC World Service from Savage Cuts http://www.petitionbuzz.com/petitions/savews', ...}
    tweets = importTweets()

    # Load the list of queries.
    # {1: ['bbc', 'world', 'servic', 'staff', 'cut'], ...}
    query_file = importQuery()

    # Build the inverted index.
    index = buildIndex(tweets)

    # Get the length of each document.
    document_length = lengthOfDocument(index, tweets)

    print("\n Preprocessing Done! \n")
    print("\n Retrieval and Ranking... \n")
    # Get length of query.
    ranking = retrieve(query_file, index, document_length)

    print("\n Retrieval and Ranking Done! \n")

    print("\n Starting to create Result File... \n")

    resultFileCreation(ranking)

    print("\n Result File Creation Done! \n")


if __name__ == "__main__":
    main()
