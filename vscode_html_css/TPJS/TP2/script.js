const div1 = document.querySelector(".gauche");
const div2 = document.querySelector(".droite");

const bdroite = document.querySelector(".bd")
const bgauche = document.querySelector(".bg")


bdroite.addEventListener('click', function (){
  return div2.appendChild(div1.firstChild)
})

bgauche.addEventListener('click', function (){
  return div1.appendChild(div2.firstChild)
})

