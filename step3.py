def step3(query, ):
    # Initialize length of query.
    length_of_query = 0
    # Initialize dictionary containing the lenths of all the Tokens.
    length_per_token = dict()
    # Initialize dictionary containing the frequency of the word in query.
    query_word_occurences = dict()
    # QUERY WORK FOR STEP 3
    # Calculating the tf-idf for the words within the Query
    for word in query:
        if word not in query_word_occurences:
                query_word_occurences[word] = 1
        else:
            query_word_occurences[word] += 1

    for word in query_word_occurences:
        # tf-idf = (0.5 + 0.5*tf_iq) * idf_i
        query_word_occurences[word] = (0.5 + (0.5 * query_word_occurences[word])) * word_idf[word]
        print("query word",word,"tf-idf",query_word_occurences[word])

    # Calculating the lenghts for all document
    doc_lenght_counter = 1
    for index, doc in word_occurences_per_token.items():
        tmp_length = 0
        for word in doc:
            tmp_length += pow(doc[word],2)
        length_per_token[doc_lenght_counter] = round(math.sqrt(tmp_length),3)
        doc_lenght_counter +=1
    print(length_per_token)

    # QUERY WORK FOR STEP 3
    # Calculating the lenghts for the query
    tmp_query_length = 0
    for word in query_word_occurences:
        print(query_word_occurences[word])
        tmp_query_length += pow(query_word_occurences[word],2)
    length_of_query = round(math.sqrt(tmp_query_length),3)
    print("Query length:",length_of_query)
    # print(word_occurences_per_token)
    sim = dict()
    tmp_dict = 1
    for index, doc in word_occurences_per_token.items():
        tmp_sim = 1
        for word in doc:
            if(word in query_word_occurences):
                tmp_sim += doc[word] * query_word_occurences[word]
                # print("query",word,query_word_occurences[word])
                # print(word,doc[word])
        
        magnitude = length_per_token[tmp_dict]*length_of_query
        dotProduct = float(tmp_sim)

        try:
            sim[tmp_dict] = dotProduct/magnitude
        except:
            print("Magnitude is",magnitude)

        # sim["D"+str(tmp_dict)+"cosSim"] = tmp_sim / x
        # print("Numerator", tmp_sim)
        #print(sim["D"+str(tmp_dict)+"cosSim"])
        # print('Denom',length_per_token["DL"+str(tmp_dict)]*length_of_query)
        # print(sim["D"+str(tmp_dict)+"cosSim"])
        tmp_dict+=1

    if verbose:
        print ('\r Dictonary:')
        print (json.dumps(dict_words, indent = 2))
        print ('-' * 40)

    return tokens