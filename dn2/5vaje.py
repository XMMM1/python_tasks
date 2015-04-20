__author__= "kristinab"

import networkx as nx
import matplotlib.pyplot as plt

print 'vaje5'
graf=nx.Graph()
graf.add_edge('Ester','Claire')
povezave=[('Alice','Bob'),
          ('Alice','Frank'),
          ('Claire','Frank'),
          ('George','Frank'),
          ('George','Denis'),
          ('Ester','Denis'),
           ('Alice','Claire'),
            ('Denis','Claire')]
graf.add_edges_from(povezave)
zenske=['Alice','Claire','Ester']
for voz in graf.nodes():
    if voz in zenske:
        graf.node[voz]['spol']='zenski'
    else:
        graf.node[voz]['spol']='moski'
graf.edge['Denis']['Claire']['odnos']='<3'
graf['Denis']['Ester']['odnos']='<3'
print graf['Denis']['Ester']
graf['Claire']['Ester']['odnos']='x'
nx.draw(graf)
plt.draw()
plt.show()

#reading and writing networks
nx.write_edgelist(graf,'graf_edgelist.txt')
nx.write_gml(graf,'graf_gml.gml')
nx.write_pajek(graf,'graf_pajek.net')


# graf=nx.Graph()
#
# #graf=nx.read_edgelist('graf_edgelist.txt')
# #graf=nx.read_gml('graf_gml.gml',relabel=True)
# graf=nx.read_pajek('graf_pajek.net')
# print graf.nodes()
# print nx.get_node_attributes(graf,'spol')
# print 'Degree: ',graf.degree()
# print graf.degree('Alice')
# #print graf.degree(3)
# print graf.neighbors('Claire')