# Import helper functions
from preprocess import filterSentence

def main():
    print("CSI 4107 - Microblog information retrieval system")

    # Example test case, will still have to load the data.
    tests = [
        "I'd very much appreciate it if 999.9% people would stop broadcasting asking me to add people on BBM.",
        "BEWARE THE BLUE MEANIES: http://bit.ly/hu8iJz #cuts #thebluemeanies",
        "999"
    ]

    for test in tests: 
        print("\n Testing string: \n\n" + test)
        filterSentence(test, True)

if __name__ == "__main__":
    main()