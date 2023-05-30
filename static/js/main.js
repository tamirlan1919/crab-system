let img = document.getElementById('img')
let video = document.querySelector('video')

console.log(img)

img.onclick = function(){
    video.setAttribute('controls','True')
    video.play()
    img.style.display = 'none'
}
