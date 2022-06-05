let btn = document.querySelector('#color');

const hideshow=document.querySelector('#hideshow');
btn.addEventListener('click',()=> { btn.style.backgroundColor = '#006400';

btn.textContent = 'Applying Algorithm..';
setTimeout(Timeout2, 5000)
setTimeout(Timeout3, 5000)  
});



let pop = document.querySelector('#popup');
pop.addEventListener('click',()=> {
swal("Unfortunate!", "Bad Time to fertilize plants", "error");
});


function hidefunction() {
    document.getElementById("hideshow").style.display="none";
    document.getElementById("color").style.display="block";
    document.getElementById("color").textContent = 'Submit';
    btn.style.backgroundColor = '#6e0025'
}


function Timeout2(){
    document.getElementById("hideshow").style.display="block";
hideshow.innerHTML=`<h4> N : </h4>
<h4> P : </h4>
<h4> K : </h4>
<button onclick="hidefunction()">OK</button>
`;
}

 function Timeout3(){
    btn.textContent = 'Result';
 }       
