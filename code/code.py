#!/bin/env python

import textrank
import plot_graph
import pickle


if __name__ == '__main__':
    print("Start plotting...")
    """
    with open('../data/data.pkl', 'r') as f:
        (x, y) = pickle.load(f)
    """

    with open('../data/reuters.txt', 'r', encoding="utf8") as f:
        test_text = f.read()

    ans, graph_info = textrank.get_keywords(test_text)
    plot_graph.visualize(graph_info)

    print("Success!")
