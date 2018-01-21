#!/bin/env python

import nltk
import numpy as np
import re
from nltk.tokenize import RegexpTokenizer
import collections
import operator
import scipy.sparse as sps
import networkx as nx


def get_keywords(raw_text, n_top_keywords = 10):
    raw_text = re.sub(r'\d+', '', raw_text)
    words = nltk.word_tokenize(raw_text)
    words = [word.lower() for word in words if word[0].isalpha()]


    #words = [w.lower() for w in text]
    wnl = nltk.WordNetLemmatizer()
    words = [wnl.lemmatize(w) for w in words]

    wordList=np.unique(words)
    wordList_filtered = np.array([word for word in wordList if word not in set(nltk.corpus.stopwords.words('english'))])

    tagged = nltk.pos_tag(wordList_filtered)


    def filter_for_tags(tagged, tags=['NN', 'JJ', 'NNP']):
        return [item for item in tagged if item[1] in tags]

    tagged = filter_for_tags(tagged)
    wordList_filtered = np.array(list(map(lambda x : x[0], tagged)))

    window_size = 3
    adj_matr = sps.lil_matrix((len(wordList_filtered), len(wordList_filtered)), dtype="float64")

    for i, word in enumerate(words):
        src = np.where(wordList_filtered == words[i])
        if len(src) > 0:
            for j in np.arange(i+1, np.min([i+window_size, len(words)])):
                dest = np.where(wordList_filtered == words[j])
                if len(dest) > 0:
                    try:
                        adj_matr[src, dest] = adj_matr[src, dest] + 1
                    except:
                        adj_matr[src, dest] = 1

    adj_matr = sps.csr_matrix(adj_matr)
    graph = nx.Graph(adj_matr)

    textrank = nx.pagerank(graph)

    sorted_by_rank = sorted(textrank.items(), key=operator.itemgetter(1))
    keywords = list(map(lambda x : x[0], sorted_by_rank[:-n_top_keywords-1:-1]))
    textrank = list(textrank.values())
    return wordList_filtered[np.array(keywords)], (textrank, adj_matr, wordList_filtered)
