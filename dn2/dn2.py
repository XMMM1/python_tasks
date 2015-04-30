__author__ = 'matej'
import networkx as nx
import matplotlib.pyplot as plt
import sys
import re

names = []
relations = []


def readFile(file):
    global names, relations
    hr = open(file, 'r')
    names = hr.readline().rstrip().split(',')
    for line in hr:
        line = line.rstrip()
        tmp = line.split('-')
        relations.append([tmp[0], tmp[1]])
    hr.close()
    return


def writeToFile(file, content):
    f = open(file, 'a')
    f.write(content)
    f.close()


def makeGraph():
    readFile('loadData.txt')
    g = nx.Graph()
    for pair in relations:
        g.add_edge(pair[0], pair[1])
    nx.draw(g)
    return g


def personFriends(G, person):
    friends = G.neighbors(str(names.index(person)))
    fr = []
    for per in friends:
        fr.append(names[int(per)])
    return fr


def familyHouse(g, house_name):
    house = []
    for id, par in g.nodes_iter(data=True):
        if par:
            if par['house'] == house_name:
                house.append(names[int(id)])
    return ', '.join(house)

def personFriendsByHouse(g, person):
    pe = {}
    for name in person:
        id = names.index(name)
        node = g.node[str(id)]
        if node:
            if node['house'] in pe:
                pe[node['house']] = pe[node['house']] + ',' + names[id]
            else:
                pe[node['house']] = names[id]
        else:
            if 'homeless' in pe:
                pe['homeless'] = pe['homeless'] + ',' + names[id]
            else:
                pe['homeless'] = names[id]
    return pe


def mostPopulatPerson(g):
    mostPopular = [0 for i in range(0, len(names))]
    for n in range(0, len(names)):
        mostPopular[n] = g.degree(str(n))
    maxFriends = max(mostPopular)
    mostPopular = [names[i] for i, x in enumerate(mostPopular) if x == maxFriends]
    # mostPopular[0] = names[mostPopular[0]]
    return mostPopular


def mainProgram():
    #-------MENU------------
    while True:
        print '1 Izpis oseb v izbrani hisi'
        print '2 Izpis znancev za izbrano osebo'
        print '3 Izpis znancev z locenimi po hisami (Romeo, Julija)'
        print '4 Izpis osebe z max znancev'
        print '5 Izhod iz programa'
        user_in = raw_input("Vas izbor: ")
        if user_in == '1':
            input_label = "Vnesite ime hise: "
            houseName = raw_input(input_label)
            while houseName not in ['House of Capulet', 'House of Montague', 'Ruling house of Verona']:
                print 'Vnesli ste napacno ime hise ki ne obstaja.'
                houseName = raw_input(input_label)
            f = familyHouse(g, houseName)
            print 'Osebe, ki prebivajo v hisi '+houseName+' so: %s' % f
            # print f
        if user_in == '2':
            input_label = "Vnesite ime: "
            name = raw_input(input_label)
            while name not in names:
                print 'Vnesli ste napacno ime, ki ni v druzinskem drevesu'
                name = raw_input(input_label)
            print 'Znanci osebe %s' % name
            f = personFriends(g, name)
            print f
        if user_in == '3':
            input_label = "Vnesite ime (Romeo, Juliet ONLY): "
            name = raw_input(input_label)
            while name not in ['Romeo', 'Juliet']:
                print 'Vnesli ste napacno ime, ki ni dovoljeno'
                name = raw_input(input_label)
            f = personFriends(g, name)
            print f
            persons = personFriendsByHouse(g, f)
            print 'Osebe v posameznih hisah ki imajo poznanstva z %s' % name
            print persons
        if user_in == '4':
            tm = mostPopulatPerson(g)
            print 'Oseba/e z max znancev je/so %s' % tm
        if user_in == '5':
            raise SystemExit


g = makeGraph()

g.node['1']['house'] = 'House of Capulet'
g.node['2']['house'] = 'House of Capulet'
g.node['3']['house'] = 'House of Capulet'
g.node['5']['house'] = 'House of Montague'
g.node['6']['house'] = 'House of Montague'
g.node['7']['house'] = 'House of Montague'
g.node['8']['house'] = 'Ruling house of Verona'
g.node['9']['house'] = 'Ruling house of Verona'
g.node['10']['house'] = 'Ruling house of Verona'

# print g.nodes(data=True)
# print g.node['1']

# print house
# plt.show()
# nx.write_edgelist(g, 'graf_edgelist.txt')
# nx.write_gml(g, 'graf_gml.gml')
# nx.write_pajek(g, 'graf_pajek.net')
mainProgram()
