const select = document.querySelector('#pays-select');
const select2 = document.querySelector('#pays2-select');
const img1 = document.querySelector('#img-1');
const img2 = document.querySelector('#img-2');

select.addEventListener('change', function(e) {
    const pays = e.target.value;
    img1.src = `plot/GHG'${pays}'.png`;
}
);

select2.addEventListener('change', function(e) {
    const pays = e.target.value;
    img2.src = `plot/ProductionOfGHGPourcentage'${pays}'.png`;
}
);