class No:
  def __init__(self, dado=None, esquerda=None, direita=None) :
    self.dado = dado
    self.esquerda = esquerda
    self.direita = direita

  def __str__(self) :
    return str(self.dado)

def imprimeArvorePreOrdem(no):
 if no == None : return
 print (no.dado)
 imprimeArvorePreOrdem(no.esquerda)
 imprimeArvorePreOrdem(no.direita)

def imprimeArvorePosOrdem(no):
 if no == None : return
 imprimeArvorePosOrdem(no.esquerda)
 imprimeArvorePosOrdem(no.direita)
 print (no.dado)

def imprimeArvoreEmOrdem(no):
 if no == None : return
 imprimeArvoreEmOrdem(no.esquerda)
 print (no.dado)
 imprimeArvoreEmOrdem(no.direita)

#Exemplo: 7 + 2 * 3
n = No('+')
n.esquerda=(No(7))
n2 = No('*')
n2.esquerda=No(2)
n2.direita=No(3)
n.direita=n2

def imprimeIdentada(no, nivel=0) :
 if no == None : return
 imprimeIdentada(no.direita, nivel+1)
 print ('   ' * nivel + str(no.dado))
 imprimeIdentada(no.esquerda, nivel+1)

print("Pré Ordem:")
imprimeArvorePreOrdem(n)
print("Em Ordem:")
imprimeArvoreEmOrdem(n)
print("Pós Ordem:")
imprimeArvorePosOrdem(n)
print("Identada:")
imprimeIdentada(n)

def insere(raiz, no):
	# Nó deve ser inserido na raiz.
	if raiz is None:
		raiz = no

	# Nó deve ser inserido na subárvore direita.
	elif raiz.dado < no.dado:
		if raiz.direita is None:
			raiz.direita = no
		else:
			insere(raiz.direita, no)

	# Nodo deve ser inserido na subárvore esquerda.
	else:
		if raiz.esquerda is None:
			raiz.esquerda = no
		else:
			insere(raiz.esquerda, no)

n = No(1)
insere(n,No(5))
insere(n,No(2))
insere(n,No(5))
insere(n,No(6))
insere(n,No(9))
print("BST:")
imprimeIdentada(n)

def busca(no, chave):
	# Trata o caso em que a chave procurada não está presente.
	if no is None:
		return None
	# A chave procurada está na raiz da árvore.
	if no.dado == chave:
		return no
	# A chave procurada é maior que a da raiz.
	if no.dado < chave:
		return busca(no.direita, chave)
	# A chave procurada é menor que a da raiz.
	return busca(no.esquerda, chave)

if busca(n,5):
	print("existe")
else:
	print("não existe")

def profundidade(no):
	if not no:
		return 0
	prof_esq = 0
	if no.esquerda:
		prof_esq = profundidade(no.esquerda)
	prof_dir = 0
	if no.direita:
		prof_dir = profundidade(no.direita)
	return 1 + max(prof_esq, prof_dir)

def balanco(no):
	prof_esq = 0
	if no.esquerda:
		prof_esq = profundidade(no.esquerda)
	prof_dir = 0
	if no.direita:
		prof_dir = profundidade(no.direita)
	return prof_dir - prof_esq

def rotacaoDireita(no):
	no.dado, no.esquerda.dado = no.esquerda.dado, no.dado
	old_direita = no.direita
	no.esquerda, no.direita = no.esquerda.esquerda, no.esquerda
	no.direita.esquerda, no.direita.direita = no.direita.direita, old_direita

def rotacaoEsquerda(no):
	no.dado, no.direita.dado = no.direita.dado, no.dado
	old_esquerda = no.esquerda
	no.esquerda, no.direita = no.direita, no.direita.direita
	no.esquerda.esquerda, no.esquerda.direita = old_esquerda, no.esquerda.esquerda

def rotacaoEsquerdaDireita(no):
	rotacaoEsquerda(no.esquerda)
	rotacaoDireita(no)

def rotacaoDireitaEsquerda(no):
	rotacaoDireita(no.direita)
	rotacaoEsquerda(no)

def balanceia(no):
	bal = balanco(no)
	if bal < -1:
		if balanco(no.esquerda) < 0:
			rotacaoDireita(no)
		else:
			rotacaoEsquerdaDireita(no)
	elif bal > 1:
		if balanco(no.direita) > 0:
			rotacaoEsquerda(no)
		else:
			rotacaoDireitaEsquerda(no)

def insereAVL(raiz, no):
	# Nó deve ser inserido na raiz.
	if raiz is None:
		raiz = no
	# Nó deve ser inserido na subárvore direita.
	elif raiz.dado < no.dado:
		if raiz.direita is None:
			raiz.direita = no
		else:
			insereAVL(raiz.direita, no)
	# Nodo deve ser inserido na subárvore esquerda.
	else:
		if raiz.esquerda is None:
			raiz.esquerda = no
		else:
			insereAVL(raiz.esquerda, no)
	balanceia(raiz)

n = No(1)
insereAVL(n,No(5))
insereAVL(n,No(2))
insereAVL(n,No(5))
insereAVL(n,No(6))
insereAVL(n,No(9))
print("AVL:")
imprimeIdentada(n)

def menorNo(no): 
	atual = no 
	while atual.esquerda is not None: 
		atual = atual.esquerda 
	return atual

def remove(raiz, chave): 
	if raiz is None: 
		return raiz 
	if chave < raiz.dado: 
		raiz.esquerda = remove(raiz.esquerda, chave) 
	elif chave > raiz.dado: 
		raiz.direita = remove(raiz.direita, chave) 
	else: 
		if raiz.esquerda is None : 
			temp = raiz.direita 
			raiz = None 
			return temp 
		elif raiz.direita is None : 
			temp = raiz.esquerda 
			raiz = None
			return temp 
		temp = menorNo(raiz.direita) 
		raiz.dado = temp.dado 
		raiz.direita = remove(raiz.direita , temp.dado) 
	return raiz 

def removeAVL(raiz, chave):
	balanceia(remove(raiz, chave))

n = No(1)
insereAVL(n,No(5))
insereAVL(n,No(2))
insereAVL(n,No(5))
insereAVL(n,No(6))
insereAVL(n,No(9))
removeAVL(n,5)
print("AVL:")
imprimeIdentada(n)