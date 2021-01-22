# Import helper functions
from preprocess import filterSentence

def main():
    print("\n CSI 4107 - Microblog information retrieval system \n")

    # Example test case, will still have to load the data.
    tests = [
        "I'd very much appreciate it if 999.9% people would stop broadcasting asking me to add people on BBM.",
        "BEWARE THE BLUE MEANIES: http://bit.ly/hu8iJz #cuts #thebluemeanies",
        "999",
        "would wouldn't couldn't"
    ]

    for test in tests: 
        print('\n Testing string: \n\n\t ' + test + '\n')
        print(' Tokenized:\n')
        filterSentence(test, True)
        print('-' * 40)

if __name__ == "__main__":
    main()