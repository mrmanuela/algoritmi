"""
    Trombetti Lisa , Procopio Saverio , Reali Manuela
    Progetto in itinere 2
    Traccia 1 - Grado di visibilità
    Implementazione del grafo
"""

from PileCode import *


class Node:
    #Nodo del grafo

    def __init__(self, id, value):

        self.id = id                #chiave del nodo
        self.value = value          #valore del nodo
        self.gradoVisibilita = 0    #grado di visibilità
        self.adjList = []           #lista di adiacenza del nodo

    def __eq__(self,other):
    #Verifica se il nodo è uguale ad other
        return self.id == other.id

    def __str__(self):
    #Stampa valore e grado di visibilità del nodo
        return "[{},{},{}]".format( self.id, self.value, self.gradoVisibilita)

    def popNode(self,list):
    #Rimuove il nodo da una lista
        for i in range(0,len(list)):
            if list[i] == self:
                list = list[:i] + list[i+1:]
                return list
        print("Non è stato trovato alcun vertice da eliminare")


class Edge:
    #Arco del grafo
    def __init__(self, tail, head):

        self.head = head        #nodo puntato dalla freccia
        self.tail = tail        #nodo da cui parte la freccia
        self.weight = 1         #peso del nodo: impostato ad 1 poichè consideriamo solo archi con peso unitario

    def __eq__(self,other):
    #Verifica se l'arco è uguale ad other
        return self.head == other.head and self.tail == other.tail

    def __str__(self):
    #Stampa coda, testa e peso dell'arco
        return "({},{},{})".format(self.tail, self.head, self.weight)

    def popEdge(self,list):
    #Rimuove l'arco da una lista
        for i in range(0,len(list)):
            if list[i] == self:
                list = list[:i] + list[i+1:]
                return list
        print("Non è stato trovato alcun arco da eliminare")


class Graph:
    #Implementazione del grafo
    def __init__(self):

        self.nodes = []                             #Lista dei nodi del grafo
        self.edges = []                             #Lista degli archi del grafo
        self.currId = 0                             #Tiene conto dell'id corrente per evitare di avere nodi con lo stesso id

    def isEmpty(self):
    #Verifica che il grafo non sia vuoto
        return len(self.nodes)!=0

    def numNodes(self):
    #Ritorna il numero di nodi contenuti nel grafo
        return len(self.nodes)

    def numEdges(self):
    #Ritorna il numero di archi contenuti nel grafo
        return len(self.edges)

    def insertNode(self, elem):
    #Aggiunge un nodo nella lista nodes e lo ritorna
        newNode = Node(self.currId, elem)
        self.nodes.append(newNode)
        self.currId += 1
        return newNode

    def deleteNode(self,node):
    #Elimina un nodo dal grafo

        #Si cancellano tutti gli archi entranti e uscenti dal nodo prima di eliminarlo
        for j in node.adjList:
            self.deleteEdge(node,j)


    def findNode(self,id):
    #Cerca il nodo nella lista nodes
        for i in range(0,len(self.nodes)):
            if  id == self.nodes[i].id:
                return self.nodes[i]
        return None

    def insertEdge(self, tail, head):
    #Inserisce l'arco nel grafo e lo ritorna
        e=Edge(tail,head)
        self.edges.append(e)
        tail.adjList.append(head)

        return e

    def findEdge(self, tail, head):
    #Cerca l'arco nella lista edges: ritorna l'arco se presente, None altrimenti
        for e in self.edges:
            if e.tail == tail and e.head == head:
                return e
        return None

    def deleteEdge(self, tail, head):
    #Cancella l'arco edge dal grafo
        e= self.findEdge(tail, head)

        tail.adjList = head.popNode(tail.adjList)
        self.edges = e.popEdge(self.edges)

    def stampa(self):
    #Stampa il grafo come lista di adiacenza

        if len(self.nodes) == 0:
            print("Il grafo è vuoto.")
            return

        for n in self.nodes:
            print(n)
            for u in n.adjList:
                print("-----> ",u)
            print("******************")