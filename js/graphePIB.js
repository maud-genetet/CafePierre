const select = document.querySelector('#pays-select');
const select2 = document.querySelector('#secteur-select');
const img1 = document.querySelector('#img-1');
const img2 = document.querySelector('#img-2');


select.addEventListener('change', function(e) {
    const pays = e.target.value;
    img1.src = `plot/GDP_H_'${pays}'.png`;
}
);

select2.addEventListener('change', function(e) {
    const secteur = e.target.value;
    img2.src = `plot/Evolution_${secteur}.png`;
}
);