var inicio
var fim

window.onload= function(){
    var x = document.getElementsByClassName('tile')
    var i;
    for (i = 0; i < x.length; i++) {
        x[i].onclick=(event)=>{
            //console.log(event.srcElement.id)
            if(inicio===undefined){
                inicio=event.srcElement.id
                event.srcElement.style.backgroundColor = "green"
            }
            else if(fim===undefined){
                fim=event.srcElement.id
                event.srcElement.style.backgroundColor = "red"
            }
        }
    } 

}

function calcular(){
    console.log('calcular'+inicio+fim)

    var request = new XMLHttpRequest()
    request.open('GET', '/calcula?inicio='+inicio+'&fim='+fim, true)
    request.send()
    request.onload=(event)=>{
        document.getElementById('map').innerHTML=event.srcElement.response
    }
}
