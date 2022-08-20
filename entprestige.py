from pyvis.network import Network
from pyvis.physics import Physics
net = Network(height='750px', width='80%')
import pandas as pd

data = pd.read_csv('~/Desktop/prestigedata.csv')


sources = data['source']
targets = data['target']
weights = data['weight']
size = data['audience.size']
label = data['label']

edge_data = zip(sources, targets, weights)

for e in edge_data:
    src = e[0]
    print(type(src))
    dst = e [1]
    w = e[2]
    asize = 0
    for i in range(int(len(label))):
        if src in label[i] :
            asize = size[i]


    net.add_node(src, src, title=src, value='audience.size')
    net.add_node(dst, dst, title=dst)
    net.add_edge(src, dst, value=w)



net.show('testentgraph.html')
net.show_buttons(filter_=['physics', 'nodes', 'edges'])