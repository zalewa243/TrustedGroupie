import os
import random

import networkx as nx
import matplotlib.pyplot as plt
from os import listdir

import sys

current_file_name = sys.argv[0].split('/')[-1]


full_file_names = {}


def extract_filename(file):
    return file.split(".")[0]  # cut extension .py


def get_file_size(file_path):
    file_path = file_path if file_path.endswith('.py') else './'+file_path+'.py'
    return os.path.getsize(file_path)


def createGraph(path="./"):
    g = nx.DiGraph()  # create direct graph
    files_to_parse = list(filter(lambda f: f.endswith(".py"), listdir(path))) # only python files
    files_to_parse.pop(files_to_parse.index(current_file_name))  # without current file

    for file_path in files_to_parse:
        g.add_node(extract_filename(file_path)+str(get_file_size(file_path)))
        find_edges_in_file(file_path, g)
    return g


def drawGraph(graph):
    nx.draw(graph, with_labels=True, font_weight='bold')
    plt.show()


def find_edges_in_file(file, g):
    with  open(file, 'r') as fr:
        for number, line in enumerate(fr): #iteruje po liniach
            if ("import" in line):
                tab = line.split()
                print(tab)
                g.add_edge(extract_filename(file)+str(get_file_size(file)), tab[1]+str(get_file_size(tab[1])))

g = createGraph()
drawGraph(g)