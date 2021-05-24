from flask import Flask,request

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

def calculaCor(n):
    if n == 0:
        return "black"
    elif n == 1:
        return "white"
    else:
        return "yellow"

@app.route("/")
def hello_world():
    html = "<p>Labirinto:</p> \
        <script src='/static/js.js'></script>"
    html += "<div id='map' style='position: center'>"
    for y in range(len(map)):
        for x in range(len(map[0])):
            print(str(x)+" "+str(y)+" "+str(map[y][x]))
            html+="<div class='tile' id="+str(x)+"_"+str(y)+" style='position: absolute; top:"+ str(20*y+100) +"px; left: "+ str(20*x+100) +"px; width: 20px; height: 20px; background-color: "+("white","black")[map[y][x]==0]+"; border: 2px solid black'></div>"
    html += "</div>"
    html += "<input type='button' value='Calcular' onclick='calcular()'></input>"
    return html

@app.route("/calcula")
def calcula():
    map = [
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,2,2,2,2,1,1,1,0],
    [0,1,1,0,1,1,1,1,1,1,0],
    [0,1,1,0,1,1,1,1,1,1,0],
    [0,1,1,0,0,1,1,1,1,1,0],
    [0,1,1,1,0,0,1,1,1,1,0],
    [0,1,1,1,1,0,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0]
    ]
    inicio=request.args.get("inicio").split('_')
    print(inicio)
    fim=request.args.get("fim").split('_')
    print(fim)
    html = ""
    for y in range(len(map)):
        for x in range(len(map[0])):
            html+="<div class='tile' id="+str(x)+"_"+str(y)+" style='position: absolute; top:"+ str(20*y+100) +"px; left: "+ str(20*x+100) +"px; width: 20px; height: 20px; background-color: "+calculaCor(map[y][x])+"; border: 2px solid black'></div>"
    return html