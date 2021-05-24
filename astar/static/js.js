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

