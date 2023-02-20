"""
    Trombetti Lisa , Procopio Saverio , Reali Manuela
    Progetto in itinere 2
    Traccia 1 - Grado di visibilità
    Grado di visibilità
"""

from PileCode import *
from Grafi import *
from Alberi import *


def minTree(start):
#Crea un albero dei cammini minimi a partire da start e lo ritorna

    T = Tree(start)  # Albero dei cammini minimi con radice start
    coda = Queue()
    coda.enqueue(T.currentNode)
    explored = []

    while coda.isEmpty() == False:
        treeNode = coda.dequeue()
        info = treeNode.info
        T.currentNode = treeNode

        if info not in explored:
            explored.append(info)

            if len(info.adjList) == 0:
                continue
            for j in info.adjList:
                if j not in explored:
                    n = T.insertAfterNode(j)
                    coda.enqueue(n)
    return T


def impostaVisibilita(T):
#Prende in ingresso un albero T di nodi e imposta il loro grado di visibilità

    root = T.root

    while T.numNodes > 1:
        list = []
        curr = root
        currMax = 0

        while len(curr.sons) != 0:
            list.append(curr.info)
            curr = curr.sons[0]
            if currMax < curr.info.value :
                currMax = curr.info.value

        list.append(curr.info)

        if len(list) == 2 or currMax <= list[-1].value:
            root.info.gradoVisibilita += 1

        curr.father.removeSon(curr)
        T.numNodes -= 1

    return root.info


def massimaVisibilita(graph):
#Calcola il nodo con massimo grado di visibilita in graph

    maxVisibilita = graph.nodes[0]                 #Nodo con massimo grado di visibilità del grafo

    for i in graph.nodes:
        if len(i.adjList) != 0:
            T = minTree(i)
            currMax = impostaVisibilita(T)
            if maxVisibilita.gradoVisibilita < currMax.gradoVisibilita:
                maxVisibilita = currMax
    return maxVisibilita



