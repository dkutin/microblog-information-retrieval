
# CSI4107 Assignment 1 - Microblog information retrieval system

## Group Members

### Dmitry Kutin - 300015920
### Dilanga Algama - 8253677
### Joshua O Erivwo - 8887065

## Reference

http://www.site.uottawa.ca/~diana/csi4107/A1_2021/A1_2021.htm

## Task Distribution

- Dmitry Kutin
	- Step 1, Step 3 (Improvements), Step 5.
- Dilanga Algama
	- Step 2, Step 3 (Initial Implementation), Step 4.
- Joshua O Erivwo
	- Step 3, README report.

## Setting up

Prerequisites: 
1. `python3` installed on your computer
2. `nltk` libaries installed (all of these can be downloaded using `python3` -> `import nltk` -> `nltk.download('corpus | tokenize | stem.porter')`: 
  * `corpus`
  * `tokenize`
  * `stem.porter`

## Execution

There are two ways of executing the program, either by running directly from the `main.py` file or running the program through `trec_eval`. 
##### Note: To ensure that the files run successfully, ensure that the prerequisites have been met.
#### Running the program directly:
  The project contains `3` folders, `5` python files, and a README file. The content included in the `assets folder` is the `tweet list`, `stop words`, and the `query` for which we would be using. The `dist folder` is where the Results text file and the trec_eval text would be stored.   
1. The first step would be to git clone the project into your computer system or download it directly from git.
2. The second step would be to open the terminal or command prompt and then go to the location of the folder (e.g: cd desktop/csi4107-assignment1-main)
3. After entering the location of the folder, then run `Python3 main.py`.
4. After running the main.py, a result text file would be printed containing the following content below:

		Topic_id  Q0  docno              rank  score                  tag   
		1         Q0  30198105513140224  1     0.588467208018523      myRun 
		1         Q0  30260724248870912  2     0.5870127971399565     myRun 
		1         Q0  32229379287289857  3     0.5311552466369023     myRun 
		
Ensure that python3 and nltk is successful installed
#### Executing the program with the use of trec_eval
1. Download trec_eval script from [trec_eval script](http://trec.nist.gov/trec_eval/).
2. Download the relevance feedback file, available [here](https://www.site.uottawa.ca/~diana/csi4107/A1_2021/Trec_microblog11-qrels.txt).
3. In the source directory, the format for the command line is: `.\trec_eval trec_rel_file` trec_top_file
4. Where trec_eval is executable, `trec_rel_file` is the relevance feedback, `trec_top_file` is the results file. 
5. The result from the compared `trec_eval` is saved under `trec_eval-results.txt`

## Functionality

   Our task was to implement an information retrieval (IR) system that collects documents (Twitter messages), which is then run on a set of test queries. A brief understanding of what our program does is that it first takes the step of importing the tweets and the queries from the 'assets folder', where the tweet list and test queries are stored and then it gets filtered (preprocessed) within the import function. After importing the text files, The following process was to build the inverted indexes of the tweets and then find the length of the document. The last step was to rank the documents through our retrieval function, creating the result text that contains the 1000 results for each query. The IR system was implemented in python. 

## Algorithms, Data Structures, and Optimizations

  Our implementation of the information retrieval system was based on the guidelines provided in the assignment. The folder contains five python files containing the function used in implementing the IR system. 

### Project Specific Files

#### Main.py:
  This file contains the main() function. In the `main()`, we started by importing the important functions that were used for implementing the IR system. The first step was to import the tweets and the queries from the `assert folder`. By importing the tweets and queries from the `asset folder`, `step1: preprocessing` was being done using the `filterSentence` that was implemented directly in the `import` function. After importing the tweets and queries from the text and then filtering them. We then moved to build the `inverted index` for the tweet. We got the `length of the document` for the indexes and tweets, which was then used to retrieve the length of the queries from the text file. In the `retrieval` function, the CosSimalarity scores were calculated and then ranked in descending order.  To understand what was happening in the `main()` function, we created a set of print statements that would notify the user when the preprocessing and the ranking of the document are done. The user then gets informed of the creation of the result file. 
#### Preprocess.py:
 This file contains the process of developing `step1:Preprocessing` and `step2:Indexing` using python. Below are the functions implemented in the `preprocess.py`
 - isNumeric(subject): Check if a string contains numerical values
 - importTweets(): imports the tweets from the collection. We first started by opening the text files, then we filter the file using our filterSentence function.
 - importQuery(): imports query from the collection. Same process as the importTweet().
 - filterSentence(sentence): Filters sentences from tweets and queries. This function builds a list of stopwords and then tokenizes each word in the sentences by removing any numerics, punctuation, or stopwords contained in the list. Each imported tweet and query runs through the NLTK's stopword list, our custom stopword list that included the URLs and abbreviations, and the provided stopword list. After this step, each word is tokenized and stemmed with Porter stemmer. Under the additional libraries, we discussed in-depth the use of tokenization, stopwords, and porter stemmer.
 - buildIndex(documents): builds the inverted index for each entry word in the vocabulary. The data structure used for the implementation was hash maps. In the realms of python development, dictionaries are equivalent to hash maps. We used dictionaries for storing the data that was being processed and used for the documents and queries. We initialized the `inverted index` and the `word_idf` as empty dictionaries that would be returned in the end. The next step stored the frequency of each word inside the already filtered documents. The final step calculated the `IDF` and the `TF-IDF` for all words contained in a document.
- lengthOfDocument(index, tweets): calculates the length of documents for each tweet.
#### Result.py: 
  This file contains the function for calculating the Cosimilarity values for the set of documents against each queries and then ranks the similarity scores in descending order. Dictionary was used as our main source for storing the values of the `query_index`,  `retrieval`,  and the `query_length`. The function comprises mainly on `for loops`. At the start, we first calculated the occurrences of the token in each query. We then moved to calculate the `TF-IDF` and the `length of the query`. After getting the necessary calculations needed, we then moved to solving the `CosSimalarity values` and then `ranking the document` according to the order that was specified.
#### write.py: 
  This file contains the procedure for implementing `step4`. The function creates a table for each of the results generated in the `result.py` and then stores it in the `dist folder` as a text file.
 
### Additional Libraries

#### Prettytable (`prettytable.py`):  
 
A helper library to format the output for the `Results.txt` file. Used in the implementation of the `write.py`.

#### NLTK:

#### PorterStemmer
Porter stemmer was an external resource that was used in the implementation of `filterSentence(sentence)`. It was used for normalizing the data for each token that was created. Stemming helps remove the morphological and inflexional endings from words in the text file.
#### Stopwords
Stopwords were also used in the preprocessing of the data. Since stopwords are common that generally do not contribute to the meaning of a sentence, we tend to filter them out which can be seen done in the `filterSentence(sentence)` function.
#### Tokenizer
We Tokenized our data in the `filterSentence(sentence)` so as to provide a link between queries and documents. Tokens are sequences of alphanumeric characters separated by nonalphanumeric characters, which are performed as part of the preprocessing (`step1` requirement).

## Discussion of final results
  The following is the evaluation of our system using the trec_eval script by comparing our results (`dist/Results.txt`) with the expected results from the provided relevance feedback file.

    runid                 	all	myRun
    num_q                 	all	49
    num_ret               	all	39091
    num_rel               	all	2640
    num_rel_ret           	all	2054
    map                   	all	0.1634
    gm_map                	all	0.0919
    Rprec                 	all	0.1856
    bpref                 	all	0.1465
    recip_rank            	all	0.3484
    iprec_at_recall_0.00  	all	0.4229
    iprec_at_recall_0.10  	all	0.3001
    iprec_at_recall_0.20  	all	0.2653
    iprec_at_recall_0.30  	all	0.2195
    iprec_at_recall_0.40  	all	0.2025
    iprec_at_recall_0.50  	all	0.1770
    iprec_at_recall_0.60  	all	0.1436
    iprec_at_recall_0.70  	all	0.1230
    iprec_at_recall_0.80  	all	0.1027
    iprec_at_recall_0.90  	all	0.0685
    iprec_at_recall_1.00  	all	0.0115
    P_5                   	all	0.1714
    P_10                  	all	0.1796
    P_15                  	all	0.1796
    P_20                  	all	0.1776
    P_30                  	all	0.1714
    P_100                 	all	0.1406
    P_200                 	all	0.1133
    P_500                 	all	0.0713
    P_1000                	all	0.0419


## First 10 Results from Queries 3 and 20

### Query 3

     3  Q0  32333726654398464  1   0.69484735460699       myRun 
 
     3  Q0  32910196598636545  2   0.6734426036041226     myRun 
 
     3  Q0  35040428893937664  3   0.5424091725376433     myRun 
 
     3  Q0  35039337598947328  4   0.5424091725376433     myRun 
 
     3  Q0  29613127372898304  5   0.5233927588038552     myRun 
 
     3  Q0  29615296666931200  6   0.5054085301107222     myRun 
 
     3  Q0  32204788955357184  7   0.48949945859699995    myRun 
 
     3  Q0  33711164877701120  8   0.47740062368197117    myRun 
 
     3  Q0  33995136060882945  9   0.47209559331399364    myRun 

     3  Q0  31167954573852672  10  0.47209559331399364    myRun 
     

### Query 20

    20        Q0  33356942797701120  1     0.8821317020383918     myRun 
    
    20        Q0  34082003779330048  2     0.7311611336720092     myRun 
    
    20        Q0  34066620821282816  3     0.7311611336720092     myRun 
    
    20        Q0  33752688764125184  4     0.7311611336720092     myRun 
    
    20        Q0  33695252271480832  5     0.7311611336720092     myRun 
    
    20        Q0  33580510970126337  6     0.7311611336720092     myRun 
    
    20        Q0  32866366780342272  7     0.7311611336720092     myRun
    
    20        Q0  32269178773708800  8     0.7311611336720092     myRun 
    
    20        Q0  32179898437218304  9     0.7311611336720092     myRun 
    
    20        Q0  31752644565409792  10    0.7311611336720092     myRun 
    
    
   ## Vocabulary
  
  Our vocabulary size was 
  
  Below is the sample of 100 tokens from our vocabulary:
  
```['bbc', 'world', 'servic', 'staff', 'cut', 'fifa', 'soccer', 'haiti', 'aristid', 'return', 'mexico', 'drug', 'war', 'diplomat', 'arrest', 'murder', 'phone', 'hack', 'british', 'politician', 'toyota', 'reca', 'egyptian', 'protest', 'attack', 'museumkubica', 'crash', 'assang', 'nobel', 'peac', 'nomin', 'oprah', 'winfrey', 'half-sist', 'known', 'unknown', 'white', 'stripe', 'breakup', 'william', 'kate', 'fax', 'save-the-da', 'cuomo', 'budget', 'super', 'bowl', 'seat', 'tsa', 'airport', 'screen', 'unemploymen', 'reduc', 'energi', 'consumpt', 'detroit', 'auto', 'global', 'warm', 'weather', 'keith', 'olbermann', 'job', 'special', 'athlet', 'state', 'union', 'dog', 'whisper', 'cesar', 'millan', "'s", 'techniqu', 'msnbc', 'rachel', 'maddow', 'sargent', 'shriver', 'tribut', 'moscow', 'bomb', 'gifford', 'recoveri', 'jordan', 'curfew', 'beck', 'piven', 'obama', 'birth', 'certifica', 'campaign', 'social', 'media', 'veneta', 'organ', 'farm', 'requir', 'evacu', 'carbon', 'monoxid']```
