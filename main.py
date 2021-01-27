# Import helper functions
from preprocess import importTweets, buildIndex

def main():
    print("\n CSI 4107 - Microblog information retrieval system \n")

    # Load the tweet list.
    # {'34952194402811904': 'Save BBC World Service from Savage Cuts http://www.petitionbuzz.com/petitions/savews', ...}
    tweets = importTweets(True)

    # Build the inverted index.
    index = buildIndex(tweets, True)

if __name__ == "__main__":
    main()