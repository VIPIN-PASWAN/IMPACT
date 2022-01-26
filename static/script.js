//Close function for messages
var messages = document.getElementById("messages_container");

setTimeout(function(){
messages.style.display = "none";
},3000);

function CloseMsgBox() {
messages.style.display = "none";
}

var today = new Date();
 var date = today.getDate()+'/'+(today.getMonth()+1)+'/'+today.getFullYear();
 const weekday = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
 const d = new Date();
 let day = weekday[d.getDay()];
 document.getElementById("currentDate").innerHTML = date.concat(",", day) ;