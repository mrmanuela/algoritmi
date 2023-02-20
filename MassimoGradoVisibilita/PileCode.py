"""
    Trombetti Lisa, Procopio Saverio, Reali Manuela
    Progetto in itinere 2
    Traccia 1 - Grado di visibilità
    Code e Pile
"""

class Stack:

    def __init__(self):
        self.s = []

    def push(self, elem):
    #Inserimento di un elemento nella pila
        self.s.insert(0, elem)

    def pop(self):
    #Eliminazione di un elemento dalla pila
        if len(self.s) == 0:
            return None
        elem = self.s[-1]
        self.s = self.s[:len(self.s)-1]
        return elem

    def top(self):
    #Ritorna il primo elemento della lista
        if len(self.s) == 0:
            return None
        return self.s[0]

    def isEmpty(self):
    #Verifica che la lista non sia vuota
        return len(self.s) == 0

    def __str__(self):
    #Stampa la pila
        print(self.s)


class Queue():

    def __init__(self):
        self.q = []

    def enqueue(self, elem):
    #Inserisce un elemento nella coda
        self.q.append(elem)

    def dequeue(self):
    #Elimina un elemento dalla coda
        if len(self.q) == 0:
            return None
        return self.q.pop(0)

    def getFirst(self):
    #Restituisce il primo elemento della coda
        if len(self.q) == 0:
            return None
        else:
            return self.q[0]

    def isEmpty(self):
    #Verifica che la coda non sia vuota
        return len(self.q) == 0

    def __str__(self):
    #Stampa la coda
        print(self.q)



