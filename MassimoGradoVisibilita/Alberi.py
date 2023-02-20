"""
    Trombetti Lisa , Procopio Saverio , Reali Manuela
    Progetto in itinere 2
    Traccia 1 - Grado di visibilità
    Albero d-ario
"""

from PileCode import *


class TreeNode:

    def __init__(self, info):

        self.father = None                  #genitore del nodo
        self.info = info                    #contiene come info un nodo del grafo
        self.sons = []                      #lista dei figli del nodo


    def removeSon(self, node):
    #Rimuove il figlio node dalla lista dei figli del nodo

        for i in range(0, len(self.sons)):
            if self.sons[i].info == node.info:
                self.sons = self.sons[:i] + self.sons[i+1:]
                return

        print("Il nodo che si vuole eliminare non esiste!")


class Tree:

    def __init__(self, radice):

        self.root = TreeNode(radice)
        self.currentNode = self.root
        self.numNodes = 1

    def insertAfterNode(self,newInfo):
    #Crea un nuovo nodo con le informazioni newInfo e lo inserisce come figlio di quello corrente

        newNode = TreeNode(newInfo)
        self.currentNode.sons.append(newNode)
        newNode.father = self.currentNode

        self.numNodes += 1

        return newNode


    def stampa(self):
    #Stampa l'albero

        pila = Stack()
        if self.root == None:
            print("Empty tree!")
            return

        pila.push([self.root, 0])  # [nodo, livello occupato dal nodo]
        while not pila.isEmpty():
            current = pila.pop()
            level = current[1]
            print("|---" * level ,current[0].info)

            for j in current[0].sons:
                pila.push([j,level +1])