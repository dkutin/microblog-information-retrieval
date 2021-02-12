# CSI4107 Assignment 1

## Group Members

### Dmitry Kutin - 300015920
### Dilanga Algama - 8253677
### Joshua O Erivwo - 8887065

## Reference

Microblog information retrieval system: http://www.site.uottawa.ca/~diana/csi4107/A1_2021/A1_2021.htm

## Task Assigned
   Each member was assigned to at least one of the steps provided by the assignment. We all contributed and helped each other with each step we gave ourselves by reviewing and improving the algorithm and data structure. Below shows how each step was divided:
Dimitry was the primary coder for step1, step3, and step5 and was peer-reviewed by Joshua and Don. Don was the primary coder for step2 and step4 and was peer-reviewed by Dimitry and Joshua. Joshua was the primary author for the README Report and contributed partially to step3,  and was peer-reviewed by Don and Dimitry. All team members were present during the evaluation of the IR system using the trec_eval

## Functionality
   Our task was to implement an information retrieval (IR) system that collects documents (Twitter messages), which is then run on a set of test queries. A brief understanding of what our program does is that it first takes the step of importing the tweets and the queries from the assets folder, where the tweet list and test queries are stored and then it gets filtered (preprocessed) within the import function. After importing the text files, The following process was to build the inverted indexes of the tweets and then find the length of the document. The last step was to rank the documents through our retrieval function, creating the result text that contains the 1000 results for each query. The IR system was implemented in python. 

## Setting up

Prerequisites: 
1. `python3` installed on your computer
2. `nltk` libaries installed (all of these can be downloaded using `python3` -> `import nltk` -> `nltk.download('corpus | tokenize | stem.porter')`: 
  * `corpus`
  * `tokenize`
  * `stem.porter`

run `python3 main.py`

## Execution
  There are two ways of executing the program, either by running directly from the main.py file or running the program through trec_eval. 
##### Note: To ensure that the files run successfully, ensure that the prerequisites have been met.
#### Running the program directly:
  The project contains three folders, five python files, and a README file. The content included in the assets folder is the tweet list, stop words, and the query for which we would be using. The dist folder is where the Results text file and the trec_eval text would be stored.   
The first step would be to git clone the project into your computer system or download it directly from git.
The second step would be to open the terminal or command prompt and then go to the location of the folder (e.g: cd desktop/csi4107-assignment1-main)
After entering the location of the folder, then run Python3 main.py.
After running the main.py, a result text file would be printed containing the following content below:
	Topic_id  Q0  docno              rank  score                  tag   
	1         Q0  30198105513140224  1     0.588467208018523      myRun 
 	1         Q0  30260724248870912  2     0.5870127971399565     myRun 
 	1         Q0  32229379287289857  3     0.5311552466369023     myRun 
Ensure that python3 and nltk is successful installed
#### Executing the program with the use of trec_eval
Download trec_eval script from trec_eval script.
Download the relevance feedback file, available here.
In the source directory, the format for the command line is: .\trec_eval trec_rel_file trec_top_file
Where trec_eval is executable, trec_rel_file is the relevance feedback, trec_top_file is the results file. 
The result from the compared trec_eval is saved under trec_eval-results.txt

## Algorithms, Data Structures, and Optimizations 
  Our implementation of the information retrieval system was based on the guidelines provided in the assignment. The folder contains five python files containing the function used in implementing the IR system. 
#### Main.py:
  This file contains the main function of the IR system. We start by importing each of the main functions that would be used for implementation. Print statements were provided for the user to understand the process that takes place. 
#### Preprocess.py:
 This file contains the process of developing step1: Preprocessing and step2: Indexing using python. Below are the functions implemented in the preprocess.py
isNumeric(subject): Check if a string contains numerical values
importTweets(): imports the tweets from the collection. We first started by opening the text files, then we filter the file using our filterSentence function.
importQuery(): imports query from the collection. Same process as the importTweet().
filterSentence(sentence): Filters sentences from tweets and queries. This function builds a list of stopwords and then tokenizes each word in the sentences by removing any numerics, punctuation, or stopwords contained in the list.
 buildIndex(documents): builds the inverted index for each entry word in the vocabulary. The data structure used for the implementation was the [hash table or access database]. We started by initializing the inverted index that would be returned. The next step stored the frequency of each word inside the already filtered documents. The final step calculated the IDF and the TF-IDF for all words contained in the documents.
lengthOfDocument(index, tweets): calculates the length of documents for each tweet.
#### Result.py: 
  This file contains the function for calculating the Cosimilarity values for the set of documents against each queries, and then ranks the similarity scores in descending order.
#### write.py: 
  This file contains the procedure for implementing step4. The function creates a table for each of the results generated in the result.py and then stores it in the dist folder as a text file.
#### prettytable.py: 
  A helper function that was used in the implementation of the write.py file.

## Discussion of final results
  The following is the evaluation of our system using the trec_eval script by comparing our results (trec_eval.txt) with the expected results from the provided relevance feedback file.

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

#### Query 3
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
     

##### Query 25
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
  
'bbc', 'world', 'servic', 'staff', 'cut', 'fifa', 'soccer', 'haiti', 'aristid', 'return', 'mexico', 'drug', 'war', 'diplomat', 'arrest', 'murder', 'phone', 'hack', 'british', 'politician', 'toyota', 'reca', 'egyptian', 'protest', 'attack', 'museumkubica', 'crash', 'assang', 'nobel', 'peac', 'nomin', 'oprah', 'winfrey', 'half-sist', 'known', 'unknown', 'white', 'stripe', 'breakup', 'william', 'kate', 'fax', 'save-the-da', 'cuomo', 'budget', 'super', 'bowl', 'seat', 'tsa', 'airport', 'screen', 'unemploymen', 'reduc', 'energi', 'consumpt', 'detroit', 'auto', 'global', 'warm', 'weather', 'keith', 'olbermann', 'job', 'special', 'athlet', 'state', 'union', 'dog', 'whisper', 'cesar', 'millan', "'s", 'techniqu', 'msnbc', 'rachel', 'maddow', 'sargent', 'shriver', 'tribut', 'moscow', 'bomb', 'gifford', 'recoveri', 'jordan', 'curfew', 'beck', 'piven', 'obama', 'birth', 'certifica', 'campaign', 'social', 'media', 'veneta', 'organ', 'farm', 'requir', 'evacu', 'carbon', 'monoxid'
