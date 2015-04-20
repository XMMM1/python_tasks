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


def PersonFriendsByHouse(g, person):
    return ''


def mostPopulatPerson(g):
    mostPopular = [0, 0]
    for n in range(0, len(names)):
        if g.degree(str(n)) > mostPopular[1]:
            mostPopular = [n, g.degree(str(n))]
    mostPopular[0] = names[mostPopular[0]]
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
        print user_in
        if user_in == '1':
            houseName = raw_input("Vnesite ime hise: ")
            while houseName not in ['House of Capulet', 'House of Montague', 'Ruling house of Verona']:
                print 'Vnesli ste napacno ime hise ki ne obstaja.'
                houseName = raw_input("Vnesite novo ime: ")
            f = familyHouse(g, houseName)
            print 'Osebe, ki prebivajo v hisi %s so:' % f
            # print f
        if user_in == '2':
            name = raw_input("Vnesite ime: ")
            while name not in names:
                print 'Vnesli ste napacno ime, ki ni v druzinskem drevesu'
                name = raw_input("Vnesite novo ime: ")
            print 'Znanci osebe %s' % name
            f = personFriends(g, name)
            print f
        if user_in == '3':
            name = raw_input("Vnesite ime (Romeo, Juliet ONLY): ")
            while name not in ['Romeo', 'Juliet']:
                print 'Vnesli ste napacno ime, ki ni dovoljeno'
                name = raw_input("Vnesite ime (Romeo, Juliet ONLY): ")
            persons = PersonFriendsByHouse(g, name)
            print 'Osebe v hisi kjer prebiva %s' % names
            print persons
        if user_in == '4':
            tm = mostPopulatPerson(g)
            print 'Oseba z max znancev je %s' % tm[0]
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
# print g.nodes('5')


# print house
# plt.show()
# nx.write_edgelist(g, 'graf_edgelist.txt')
# nx.write_gml(g, 'graf_gml.gml')
# nx.write_pajek(g, 'graf_pajek.net')
mainProgram()
