let btn = document.querySelector('#color');
let OK = document.querySelector(".answer")
OK.style.display="none";
 const hideshow=document.querySelector('#hideshow');

 btn.addEventListener('click',()=> { 
    btn.style.backgroundColor = '#006400';
    btn.textContent = 'Applying Algorithm..';
//  setTimeout(Timeout3, 5000)  

 });


let pop = document.querySelector('#popup');
pop.addEventListener('click',()=> {
swal("Unfortunate!", "Bad Time to fertilize plants", "error");
});



 function Timeout3(){
    document.getElementById("color").style.display="none";
    document.getElementById("answer2").style.display="block";
    
 }       

 function hideok(){
     OK.style.display="none";
     document.getElementById("color").style.display="block";
    document.getElementById("color").textContent = 'Submit';
    btn.style.backgroundColor = '#6e0025'
 }