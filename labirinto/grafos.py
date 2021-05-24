grafo = { "A" : ["B"],
          "B" : ["C", "D"],
          "C" : ["B", "E"],
          "D" : ["A"],
          "E" : ["B"]
        }
		
print(grafo["A"])
def dfs_recursiva(grafo, vertice, visitados,nivel):
	visitados.add(vertice)
	print(' '*nivel+vertice)
	for vizinho in grafo[vertice]:
		if vizinho not in visitados:
			dfs_recursiva(grafo, vizinho, visitados, nivel+1)
			
def dfs(grafo, vertice):
	visitados = set()
	dfs_recursiva(grafo, vertice, visitados,0)
	return visitados

print(dfs(grafo, 'A'))

def dfs_iterativa(grafo, vertice_fonte, vertice_fim = None):
	visitados=set()
	visitados.add(vertice_fonte)
	falta_visitar = [vertice_fonte]
	while falta_visitar:
		vertice = falta_visitar.pop()
		for vizinho in grafo[vertice]:
			print("visitados: " + str(visitados))
			if vizinho not in visitados:
				visitados.add(vizinho)
				falta_visitar.append(vizinho)
			if vizinho==vertice_fim:
				return visitados
			print("falta visitar: " + str(falta_visitar))
dfs_iterativa(grafo, 'A')
def bfs(grafo, vertice_fonte, vertice_fim = None):
	visitados, fila = set(), [vertice_fonte]
	while fila:
		vertice = fila.pop(0)
		if vertice not in visitados:
			visitados.add(vertice)
			fila.extend(set(grafo[vertice]) - visitados)
		if vertice == vertice_fim:
			return visitados
	return visitados
print(bfs(grafo, 'A'))