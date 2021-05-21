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
    def getDadoCabeca(self):
        if self.cabeca == None:
            return None
        return self.cabeca.getDado()
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
    #Verificar se existe um determinado valor na lista
    def buscar(self, valor):
        contador = 0
        elemento = self.cabeca
        while elemento != None:
            if elemento.dado == valor:
                return contador
            contador = contador + 1
            elemento = elemento.getProx()
        return -1
    #Remover nós da lista
    def removerTodos(self, dado):
        elemento = self.cabeca
        while elemento != None and elemento.getDado() == dado:
            self.cabeca = elemento.getProx()
            elemento = self.cabeca
        while elemento != None:                
            if elemento.getProx()!=None and elemento.getProx().getDado() == dado:
                elemento.setProx(elemento.getProx().getProx())
            elemento = elemento.getProx()
    #Remover um nó da lista
    def remover(self, dado):
        elemento = self.cabeca
        if elemento != None and elemento.getDado() == dado:
            self.cabeca = elemento.getProx()
            return
        while elemento != None:                
            if elemento.getProx()!=None and elemento.getProx().getDado() == dado:
                elemento.setProx(elemento.getProx().getProx())
                break
            elemento = elemento.getProx()
    #Remover um nó da lista
    def removerCabeca(self):
        if self.cabeca != None:
            elemento = self.cabeca.getDado()
            self.cabeca = self.cabeca.getProx()
            return elemento

#lista = ListaEncadeada()
#lista.add(No("José"))
#lista.add(No("Fernando"))
#lista.add(No("José"))
#lista.add(No("José"))
#print (lista)
#print (lista.contar())
#print (lista.buscar("Fernando"))
#lista.remover("José")
#print (lista.removerCabeca())
#print (lista)

#Adicionar um nó em uma posição específica da lista

#PILHA
#empilha: Adiciona um elemento no topo
#desempilha: Remove elemento do topo, retornando seu valor
#vazio: Retorna se a pilha está vazia
#topo: Retorna o elemento do topo

class Pilha:
    def __init__(self):
        self.lista = ListaEncadeada()
    def __str__(self):
        txt='['
        noAtual = self.lista.cabeca
        while noAtual != None:
            txt = txt+str(noAtual.getDado())
            if noAtual.getProx() != None:
                txt = txt + ', '
            noAtual=noAtual.getProx()
        txt = txt + ']'
        return txt
    def empilhar(self, dado):
        no=No(dado)
        self.lista.add(no)
    def desempilhar(self):
        return self.lista.removerCabeca()
    def vazia(self):
        return self.lista.isEmpty()
    def topo(self):
        return self.lista.getDadoCabeca()

pilha = Pilha()
pilha.empilhar("0")
pilha.empilhar("1")
pilha.empilhar("2")
pilha.empilhar("3")
#print(pilha)
#print(pilha.desempilhar())
#print(pilha.topo())

def calculaPolonesa(exp):
    p = Pilha()
    op1 = 0
    op2 = 0
    for i in exp.split(","):
        if i == "+":
           op2 = p.desempilhar()
           op1 = p.desempilhar()
           p.empilhar(op1+op2)
        elif i == "-":
            op2 = p.desempilhar()
            op1 = p.desempilhar()
            p.empilhar(op1-op2)
        elif i == "*":
            op2 = p.desempilhar()
            op1 = p.desempilhar()
            p.empilhar(op1*op2)
        elif i == "/":
            op2 = p.desempilhar()
            op1 = p.desempilhar()
            p.empilhar(op1/op2)
        else:
            p.empilhar(int(i))
    return p.topo()

print(calculaPolonesa("2,3,4,+,*,5,/,6,-"))

vetor = [None]*10
print(vetor)
print(len(vetor))