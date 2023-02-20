"""
    Trombetti Lisa , Procopio Saverio , Reali Manuela
    Progetto in itinere 2
    Traccia 1 - Grado di visibilità
    Demo
"""

from GradoVisibilita import *
from random import randint
from time import time

def generateRandomGraph(nodes):
#Genera un grafo diretto aciclico con value dei nodi random

    graph = Graph()
    curr = graph.insertNode(randint(1,100))

    for i in range(0,nodes):
        n = graph.insertNode(randint(1,100))
        graph.insertEdge(curr,n)
        curr = n

    return graph


def test(nodes):

    tMinTree = 0
    tImpostaVisibilita = 0
    tMassimaVisibilita = 0

    for i in range(0,20):
        graph = generateRandomGraph(nodes)

        start = time()
        T = minTree(graph.nodes[0])
        tMinTree += time() - start

        start = time()
        impostaVisibilita(T)
        tImpostaVisibilita += time() - start

        start = time()
        massimaVisibilita(graph)
        tMassimaVisibilita += time() - start

    print("Tempo medio minTree : ",tMinTree/20)
    print("Tempo medio impostaVisibilita : ",tImpostaVisibilita/20)
    print("Tempo medio massimaVisibilita : ",tMassimaVisibilita/20)

#-----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    print("---Test dei tempi di esecuzione degli algoritmi ---")
    test(50)

    print("\n---Test grado visibilita---")
    g = generateRandomGraph(10)
    print("Nodo con massimo grado di visibilita nel grafo : ",massimaVisibilita(g))
    minTree(g.nodes[0]).stampa()