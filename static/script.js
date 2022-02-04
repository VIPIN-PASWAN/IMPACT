var messages = document.getElementById("messages_container");

setTimeout(function(){
//messages.style.display = "none";
$('.alert').alert('close');
},3000);

let today = new Date();
let date = today.getDate() + '/' + (today.getMonth() + 1) + '/' + today.getFullYear();
const weekday = ["Sun","Mon","Tue","Wed","Thur","Fri","Sat"];
 const d = new Date();
 let day = weekday[d.getDay()];
 document.getElementById("currentDate").innerHTML = date.concat(",", day) ;

 let previews=document.getElementsByClassName('preview');
      Array.from(previews).forEach((element)=>{
          element.innerHTML=element.innerText;
      })