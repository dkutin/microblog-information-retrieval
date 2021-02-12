# CSI4107 Assignment 1

## Group Members

### Dmitry Kutin - 300015920
### Dilanga Algama - 8253677
### Joshua O Erivwo - 8887065

## Reference

Microblog information retrieval system: http://www.site.uottawa.ca/~diana/csi4107/A1_2021/A1_2021.htm

## Functionality

## Setting up

Prerequisites: 
1. `python3` installed on your computer
2. `nltk` libaries installed (all of these can be downloaded using `python3` -> `import nltk` -> `nltk.download('corpus | tokenize | stem.porter')`: 
  * `corpus`
  * `tokenize`
  * `stem.porter`

run `python3 main.py`

## Execution

## Algorithms, Data Structures, and Optimizations 


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
