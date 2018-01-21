#!/bin/env python

import networkx as nx
import scipy.sparse as sps    
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def visualize(graph_info, n_top_keywords = 10):
    textrank, adj_matr, wordList_filtered = graph_info

    pivot = sorted(textrank)[-n_top_keywords]
    textrank = np.array(textrank)
    textrank[textrank < pivot] = -1
    textrank += 1
    textrank *= 150
    textrank += 20

    color_map = np.empty(textrank.shape[0], dtype='<U15')
    color_map[textrank > 20] = 'red'
    color_map[textrank <= 20] = 'blue'

    sizes_map = np.empty(textrank.shape[0])
    sizes_map[textrank > 20] = 20
    sizes_map[textrank <= 20] = 7

    N=adj_matr.shape[0] # number of nodes
    gow = nx.Graph(adj_matr)

    #f, ax = plt.subplots(figsize=(20,20))
    plt.figure(figsize=(20,20))
    #pos=nx.spring_layout(gow, k= 1/np.sqrt(N)*35,iterations=5,weight=0.2) # positions for all nodes
    pos = nx.spring_layout(gow,scale=2, iterations=5, k = 2)#nx.spectral_layout(gow, scale = 20)
    nx.draw_networkx_nodes(gow,pos,
                           node_list=np.arange(len(wordList_filtered)),
                           node_color=color_map,
                           node_size=list(textrank),
                       alpha=0.9)


    # edges
    nx.draw_networkx_edges(gow,pos,width=0.5,arrows=True,alpha=0.5)

    # some math labels
    other_nodes_inds = np.where(textrank <= 20)[0]
    key_nodes_inds = np.where(textrank > 20)[0]
    nx.draw_networkx_labels(gow,pos,dict(zip(other_nodes_inds, wordList_filtered[other_nodes_inds])),font_size=15)
    nx.draw_networkx_labels(gow,pos,dict(zip(key_nodes_inds, wordList_filtered[key_nodes_inds])),font_size=40)

    plt.savefig('../latex/textrank_example.png')
