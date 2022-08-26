from copyreg import constructor
from pyvis.network import Network
net = Network(height='90%', width='90%')
import pandas as pd
import networkx as nx

data = pd.read_csv('~/Desktop/prestigedata8.26.csv')

sources = data['source']
targets = data['target']
weights = data['weight']
size = data['audience.size']
label = data['label']

edge_data = zip(sources, targets, weights)

for e in edge_data:
    src = e[0]
    dst = e[1] 
    w = e[2]

    net.add_node(src, src, title=src)
    net.add_node(dst, dst, title=dst)
    net.add_edge(src, dst, value=w)

net.show_buttons(filter_=True)
net.show('testentgraph.html')
