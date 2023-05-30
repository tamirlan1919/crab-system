let img = document.getElementById('img')
let video = document.querySelector('video')

console.log(img)

img.onclick = function(){
    video.setAttribute('controls','True')
    video.play()
    img.style.display = 'none'
}


let selectElement = document.getElementById("city-select");
      
selectElement.addEventListener("change", function() {
  let selectedOption = selectElement.options[selectElement.selectedIndex];

  let phoneNumberElement = document.getElementById("phone-number");
  phoneNumberElement.textContent = selectedOption.getAttribute("data-phone");
});

function opennav(){

document.getElementById('modal-nav').style.display = 'block'
document.getElementById('list').style.display = 'none'
document.getElementById('exit').style.display = 'block'

}

function closenav(){
document.getElementById('modal-nav').style.display = 'none'
document.getElementById('exit').style.display = 'none'
document.getElementById('list').style.display = 'block'
}
function closebut(){

document.getElementById('modal-nav').style.display = 'none'
document.getElementById('list').style.display = 'block'
}

let ema = document.querySelector('.ema')



let modal = document.getElementById("myModal");
let btn = document.getElementById("openModalBtn");
let btn2 = document.getElementById("openModalBtnn");
let btn3 = document.getElementById("openModalBtnnn");
let span = document.getElementsByClassName("close")[0];
let form = document.getElementById("myForm");

function bb(){
  modal.style.display = "block";
}

btn.addEventListener('click',bb)


btn2.onclick = function(){
    modal.style.display = "block";

}



btn3.onclick = function(){
  modal.style.display = "block";

}

span.onclick = function() {
  modal.style.display = "none";
};

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};
