const select = document.querySelector('#pays-select');

const img1 = document.querySelector('#img-1');



select.addEventListener('change', function(e) {
    const pays = e.target.value;
    img1.src = `plot/GDP_H_'${pays}'.png`;
}
); 

