let butt_genergate_url = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type #butt_genergate_url');
let butt_genergate_vcard = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type #butt_genergate_vcard');
let butt_genergate_text = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type #butt_genergate_text');
let butt_genergate_email = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type #butt_genergate_email');
let butt_genergate_wifi = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type #butt_genergate_wifi');
let butt_genergate_facebook = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type #butt_genergate_facebook');
let butt_genergate_pdf = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type #butt_genergate_pdf');
let butt_genergate_image = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type #butt_genergate_image');
// =========url===================
let textarea_input = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type #url');
// =========vcard==========
let first_name = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type .container_input_row .col_chill #first_name');
let last_name = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type .container_input_row .col_chill #last_name');
let mobile = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type .container_input_row .col_chill #mobile');
let phone = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type .container_input_row .col_chill #phone');
let fax = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type .container_input_row .col_chill #fax');
let email = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type .container_input_row .col_chill #email');
let company = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type .container_input_row .col_chill #company');
let job = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type .container_input_row .col_chill #job');
let street = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type .container_input_row .col_chill #street');
let city = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type .container_input_row .col_chill #city');
let zip = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type .container_input_row .col_chill #zip');
let state = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type .container_input_row .col_chill #state');
let country = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type .container_input_row .col_chill #country');
let website = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type .container_input_row .col_chill #website');
// ========================


butt_genergate_url.addEventListener('click', send_url);
butt_genergate_vcard.addEventListener('click', send_vcard);


function send_url() {
   let send_url = {
       'type':'url',
       'data':{
           'content': btoa(textarea_input.value),
       }
   }
//    console.log(JSON.stringify(send_url))
}

function send_vcard(){
    let send_vcard = {
        'type':'vcard',
        'data':{
            'name':btoa(last_name.value + first_name.value),
            'contact':{
                'mobile':btoa(mobile.value),
                'phone':btoa(phone.value),
                'fax':btoa(fax.value),
            },
            'email':btoa(email.value),
            'company':{
                'company_ch':btoa(company.value),
                'job':btoa(job.value)
            },
            'street':btoa(street.value),
            'city':{
                'city':btoa(city.value),
                'zip':btoa(zip.value)
            },
            'state':btoa(state.value),
            'country':btoa(country.value),
            'website':btoa(website.value)
        }
    }
       console.log(JSON.stringify(send_vcard))
}




