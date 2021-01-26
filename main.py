# Import helper functions
from preprocess import *

def main():
    print("\n CSI 4107 - Microblog information retrieval system \n")

    # Example test case, will still have to load the data.
    testDocs = [
        "I'd very much appreciate it if 999.9% people would stop broadcasting asking me to add people on BBM.",
        "BEWARE THE BLUE MEANIES PEOPLE: http://bit.ly/hu8iJz #cuts #thebluemeanies",
        "999",
        "would wouldn't couldn't",
        "Sri Lanka hello",
        "Sri Lanka post",
        "South Korea hello"
    ]

    documents = []

    # {'34952194402811904': 'Save BBC World Service from Savage Cuts http://www.petitionbuzz.com/petitions/savews', ...}
    for test in testDocs: 
        print('\n Testing string: \n\n\t ' + test + '\n')
        print(' Tokenized:\n')
        tokens = filterSentence(test, True)
        print("start",tokens)
        documents.append(tokens)
        print('-' * 40)
    
    index = buildIndex(documents, True)

if __name__ == "__main__":
    main()