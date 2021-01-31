from collections import defaultdict

def create_index (data):
        index = defaultdict(list)
        for i, tokens in enumerate(data):
            for token in tokens:
                index[token].append(i)
        return index