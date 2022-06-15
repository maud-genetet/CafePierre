const select = document.querySelector('#secteur-select');
const select2 = document.querySelector('#secteur2-select');
const img1 = document.querySelector('#img-1');
const img2 = document.querySelector('#img-2');



select.addEventListener('change', function(e) {
    const select = e.target.value;
    img1.src = `plot/Evolution_${select}.png`;
}
); 

select2.addEventListener('change', function(e) {
    const secteur = e.target.value;
    img2.src = `plot/Pourcentage${secteur}.png`;
}
);

