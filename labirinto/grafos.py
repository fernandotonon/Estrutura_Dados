def verificaVisitado(lista,valor):
	for i in lista:
		if i[0]==valor:
			return True
	return False

def reconstroiCaminho(visitados):
	resultado=[]
	atual = visitados.pop()
	pai = atual[1]
	while pai:
		resultado.append(atual[0])
		pai = atual[1]
		for i in range(len(visitados)):
			if visitados[i][0] == pai:
				atual=visitados.pop(i)
				break
	return resultado

def listaVisitados(visitados):
	resultado=[]
	while visitados:
		atual = visitados.pop()
		resultado.append(atual[0])
	return resultado

def dfs_iterativa(grafo, vertice_fonte, vertice_fim = None):
	visitados=[]
	visitados.append([vertice_fonte,None])
	falta_visitar = [vertice_fonte]
	while falta_visitar:
		vertice = falta_visitar.pop()
		for vizinho in grafo[vertice]:
			if not verificaVisitado(visitados, vizinho):
				visitados.append([vizinho,vertice])
				falta_visitar.append(vizinho)
			if vizinho==vertice_fim:
				return reconstroiCaminho(visitados.copy()), listaVisitados(visitados)

def bfs(grafo, vertice_fonte, vertice_fim = None):
	visitados, fila = [], [vertice_fonte]
	visitados.append([vertice_fonte,None])
	while fila:
		vertice = fila.pop(0)
		for vizinho in grafo[vertice]:
			print("visitados: " + str(visitados))
			if not verificaVisitado(visitados, vizinho):
				visitados.append([vizinho,vertice])
				fila.append(vizinho)
			if vizinho==vertice_fim:
				return reconstroiCaminho(visitados.copy()), listaVisitados(visitados)