let container_type_details = document.querySelectorAll('.container_menu_input_right .container_input_type');
let container_type = document.querySelectorAll('.container_menu_type_left .container_qr_type');
let header = document.querySelector('.header');

container_type.forEach(type => {
    type.addEventListener('click', () => {
        container_type.forEach(remove_type => {
            remove_type.classList.remove('active');
        })
        let name = type.getAttribute('data-name');
        container_type_details.forEach(type_details => {
            let target = type_details.getAttribute('data-target');
            type_details.classList.remove('active');
            if (name == target) {
                type_details.classList.add('active');
                type.classList.add('active');
            }
        })
    })
})

window.addEventListener('scroll',sh_hiddem);
let cur_y = 0;
function sh_hiddem(){
    let y = scrollY;
    if(y>80 && y>cur_y){
        header.classList.add('hidden');
        cur_y = y;
    }else if(y<cur_y && y<80){
        header.classList.remove('hidden');
        cur_y = y;
    }
}