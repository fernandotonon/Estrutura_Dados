class No:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None
    def getDado(self):
        return self.dado
    def setDado(self, dado):
        self.dado = dado
    def getProx(self):
        return self.prox
    def setProx(self, prox):
        self.prox = prox

class ListaEncadeada:
    def __init__(self):
        self.cabeca=None
    def __str__(self):
        txt='['
        noAtual = self.cabeca
        while noAtual != None:
            txt = txt+str(noAtual.getDado())
            if noAtual.getProx() != None:
                txt = txt + ', '
            noAtual=noAtual.getProx()
        txt = txt + ']'
        return txt
    def isEmpty(self):
        return self.cabeca == None
    #Adicionar novo nó no início
    def add(self, elemento):
        elemento.setProx(self.cabeca)
        self.cabeca = elemento
    #Contar o tamanho
    def contar(self):
        contador = 0
        elemento = self.cabeca
        while elemento != None:
            contador = contador + 1
            elemento = elemento.getProx()
        return contador

lista = ListaEncadeada()
lista.add(No("Fernando"))
lista.add(No("José"))
lista.add(No("José"))
print (lista)
print (lista.contar())

#Verificar se existe um determinado valor na lista
#Remover um nó da lista
#Adicionar um nó em uma posição específica da lista