const select = document.querySelector('#pays-select');
const select2 = document.querySelector('#pays2-select');
const select3 = document.querySelector('#secteur-select');
const img1 = document.querySelector('#img-1');
const img2 = document.querySelector('#img-2');
const img3 = document.querySelector('#img-3');


select.addEventListener('change', function(e) {
    const pays = e.target.value;
    img1.src = `plot/primaryEnergyConsumption'${pays}'.png`;
}
);

select2.addEventListener('change', function(e) {
    const secteur = e.target.value;
    img2.src = `plot/primaryEnergyProduction'${secteur}'.png`;
}
);

select3.addEventListener('change', function(e) {
    const secteur = e.target.value;
    img3.src = `plot/ProductionOfEnergyWithTheSource${secteur}.png`;
}
);