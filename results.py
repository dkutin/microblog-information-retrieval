import math
import json

def retrieve(query_list, inverted_index, document_length, verbose = False):
    # Tokenize query for input to index.
    # ranking[query_num][document_id] = cosSim(di, q)
    query_tfidf = dict()
    ranking = dict()

    for query_num, query in query_list.items():
        # Store the number of occurences for each token in the query.
        query_index = dict()
        # Store the tfidf value of each token
        retrieval = dict()
        # Store the magnitude of each query vector.
        query_length = dict()

        # Calculate the occurences of token in query.
        for token in query:
            if token not in query_index:
                query_index[token]=1
            else:
                query_index[token]+=1

        # Calculate the tfidf for each token in query.
        for token, occurences in query_index.items():
            try:
                for document_id, tfidf in inverted_index[token].items():
                    # TODO: Set distinct query tfidf per document.
                    retrieval[token] = 0.5 + (0.5 * (occurences / max(query_index.values())) * tfidf)
                    break
            except KeyError:
                retrieval[token] = 0.0

            query_tfidf[query_num] = retrieval

        # Calculate the length of the query.
        for query_num, tokens in query_tfidf.items():
            query_len = 0.0
            for token, tfidf in tokens.items():
                query_len += pow(tfidf, 2)

            query_length[query_num] = round(math.sqrt(query_len), 3)

    # Calculate the CosSim of each document, against each query.
    for query_no, query_token_info in query_tfidf.items():
        # Store the CosSim of each Document & current query.
        doc_cossim = dict()
        for document_id, document_len in document_length.items():
            dotproduct = 0.0
            for token, tfidf in query_token_info.items():
                # Try to index the inverted index to get tfidf for current token, document.
                try:
                    document_dp = inverted_index[token][document_id]
                except KeyError:
                    continue

                # Calculate the Dot Product Numerator.
                dotproduct += document_dp * tfidf

            # If the dotproduct is zero, don't add it to the list.
            if (dotproduct == 0.0):
                continue
            # Calculate the full Dot Product.
            try:
                doc_cossim[document_id] = dotproduct / (document_len * query_length[query_no])
            except ZeroDivisionError:
                continue

        # Put the ranking of Documents in Descending order into ranking.
        ranking[query_no] = {k: v for k, v in sorted(doc_cossim.items(), key=lambda doc_cossim: doc_cossim[1], reverse=True)}

    if (verbose):
        print('Query Ranking')
        print(json.dumps(ranking, indent = 2))
        print("-" * 40)

    return ranking
