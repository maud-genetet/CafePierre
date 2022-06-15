const logo = document.querySelector('.logo img');
const nom = document.querySelector('.containerLogoNom h1');
const haut = document.querySelector('.haut');

window.addEventListener('scroll', () => {
    if (window.scrollY>haut.clientHeight){
        nom.style.color =  "#000000";
        logo.style.filter = "grayscale() invert()";
    }
    else {
        nom.style.color = "#ecedd4";
        logo.style.filter = "none";
    }
})