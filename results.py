from preprocess import filterSentence
import collections
import math

def retrieve(query_list, inverted_index, verbose = False):
    # Tokenize query for input to index.
    # ranking[query_num][document_id] = cosSim(di, q)
    ranking = dict()

    for query_num, query in query_list.items():
        retrieval = dict()
        query_index = dict()
        # Occurences of token in query.
        for token in query:
            if token not in query_index:
                query_index[token]=1
            else:
                query_index[token]+=1

        for token, occurences in query_index.items():
            for document_id, tfidf in inverted_index[token].items():
                # TODO: Set distinct query tfidf per document.
                retrieval[token] = 0.5 + (0.5 * (occurences / max(query_index.values())) * tfidf)
                break

        ranking[query_num] = retrieval

        query_len = 0.0
        for query, tokens in ranking.items():
            for token, tfidf in tokens.items():
                query_len += pow(tfidf, 2)

            query_len = round(math.sqrt(query_len), 3)

            ranking[query_num] = query_len

    # TODO: Calculate Cosine Similiarity.

    # Return: Ordered Ranking[query_no] = {d1 : cosSim, d2 : cosSim, ...}

    return ranking

