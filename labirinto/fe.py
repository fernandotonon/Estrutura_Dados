from flask import Flask,request
import grafos

app = Flask(__name__)

map = [
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,0,1,1,1,1,1,1,0],
    [0,1,1,0,1,1,1,1,1,1,0],
    [0,1,1,0,0,1,1,1,1,1,0],
    [0,1,1,1,0,0,1,1,1,1,0],
    [0,1,1,1,1,0,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0]
    ]

#cria grafo
grafo = {}
for y in range(len(map)):
    for x in range(len(map[0])):
        grafo[str(x)+"_"+str(y)]=[]
        if y < len(map)-1 and map[y+1][x]==1:
            grafo[str(x)+"_"+str(y)]+=[str(x)+"_"+str(y+1)]
        if x < len(map[0])-1 and map[y][x+1]==1:
            grafo[str(x)+"_"+str(y)]+=[str(x+1)+"_"+str(y)]
        if x > 0 and map[y][x-1]==1:
            grafo[str(x)+"_"+str(y)]+=[str(x-1)+"_"+str(y)]
        if y > 0 and map[y-1][x]==1:
            grafo[str(x)+"_"+str(y)]+=[str(x)+"_"+str(y-1)]

def calculaCor(x,y,resultado=None,visitados=None):
    if resultado and (str(x)+"_"+str(y)) in resultado:
        return "purple"
    if visitados and (str(x)+"_"+str(y)) in visitados:
        return "yellow"
    n=map[y][x]
    if n == 0:
        return "black"
    elif n == 1:
        return "white"
    else:
        return "yellow"

@app.route("/")
def hello_world():
    html = "<h1>Labirinto:</h1> \
        <script src='/static/js.js'></script>"
    html += "<div id='map' style='position: center'>"
    for y in range(len(map)):
        for x in range(len(map[0])):
            print(str(x)+" "+str(y)+" "+str(map[y][x]))
            html+="<div class='tile' id="+str(x)+"_"+str(y)+" style='position: absolute; top:"+ str(20*y+100) +"px; left: "+ str(20*x+100) +"px; width: 20px; height: 20px; background-color: "+("white","black")[map[y][x]==0]+"; border: 2px solid black'></div>"
    html += "</div>"
    html += "<input type='button' value='Reset' onclick='location.reload()'></input>"
    html += "<input type='button' value='Calcular BFS' onclick='calcular(\"bfs\")'></input>"
    html += "<input type='button' value='Calcular DFS' onclick='calcular(\"dfs\")'></input>"
    return html

@app.route("/calcula")
def calcula():
    inicio=request.args.get("inicio")
    fim=request.args.get("fim")
    algo=request.args.get("algo")
    resultado = []
    visitados = []
    if algo == "bfs":
        resultado, visitados = grafos.bfs(grafo,inicio,fim)
    elif algo == "dfs":
        resultado, visitados = grafos.dfs_iterativa(grafo,inicio,fim)

    print("resultado")
    print(resultado)
    html = ""+algo+ " Inicio: " + inicio + " Fim: "+fim +" Resultado: "+str(resultado)
    for y in range(len(map)):
        for x in range(len(map[0])):
            html+="<div class='tile' id="+str(x)+"_"+str(y)+" style='position: absolute; top:"+ str(20*y+100) +"px; left: "+ str(20*x+100) +"px; width: 20px; height: 20px; background-color: "+calculaCor(x,y,resultado,visitados)+"; border: 2px solid black'></div>"
    return html