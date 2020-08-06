let counter = 0;
let minutes = 0;
let hours = 0;
function count(){
    counter++;
    document.querySelector('#counter').innerHTML = counter;
    if(counter==60){
  
        min();
        
    }
    if(minutes>60){
 
        hour();
    
    }
}

function min(){
    minutes++;
    document.querySelector('#min').innerHTML = minutes;
    counter=0;
}

function hour(){
    hours++;
    document.querySelector('#hour').innerHTML = hours;
    min=0;
}

document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('button').onclick = count;
    setInterval(count,1000);
 
    
});