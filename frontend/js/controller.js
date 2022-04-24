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
let email_vcard = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type .container_input_row .col_chill #email_vcard');
let company = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type .container_input_row .col_chill #company');
let job = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type .container_input_row .col_chill #job');
let street = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type .container_input_row .col_chill #street');
let city = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type .container_input_row .col_chill #city');
let zip = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type .container_input_row .col_chill #zip');
let state = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type .container_input_row .col_chill #state');
let country = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type .container_input_row .col_chill #country');
let website = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type .container_input_row .col_chill #website');
// =========== text =============
let text = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type #text');
// ============= email ===============
let email_email = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type .container_input_row .col_chill #email_email');
let subject = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type .container_input_row .col_chill #subject');
let mess = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type .container_input_row .col_chill #mess');
// ================== wifi ==============
let network_name = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type .container_input_row .col_chill #SSID');
let password = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type .container_input_row .col_chill #password');
let ssid_hidden = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type .container_input_row .col_chill #SSID_hidden');
let select_none = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type .container_input_row .col_chill label #select_none');
let select_WPA_WPA2 = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type .container_input_row .col_chill label #select_WPA_WPA2');
let select_WEP = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type .container_input_row .col_chill label #select_WEP');
// ==================== facebook ===============
let url_fb = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type .container_input_row .col_chill #url_fb');
let name_fb = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type .container_input_row .col_chill #name_fb');
let title_fb = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type .container_input_row .col_chill #title_fb');
let website_fb = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type .container_input_row .col_chill #website_fb');
// ================ ===============
let img_qr = document.querySelector('.home .container_right_output .container_img_qr #qr')

// ======== event genergate =========
butt_genergate_url.addEventListener('click', send_url);
// butt_genergate_url.addEventListener('click', get_Data);
butt_genergate_vcard.addEventListener('click', send_vcard);
butt_genergate_text.addEventListener('click', send_text);
butt_genergate_email.addEventListener('click', send_email);
butt_genergate_wifi.addEventListener('click', send_wifi);
butt_genergate_facebook.addEventListener('click', send_fb);


// ======= funct url==============
function send_url() {
    let send_url = {
        'type': 'url',
        'data': {
            'content': btoa(textarea_input.value),
        }
    }
    //    console.log(JSON.stringify(send_url))
    reqapi(send_url)

}
// ========== funct vcard ========
function send_vcard() {
    let send_vcard = {
        'type': 'vcard',
        'data': {
            'fname': btoa(first_name.value),
            'lname': btoa(last_name.value),
            'mobile': btoa(mobile.value),
            'phone': btoa(phone.value),
            'fax': btoa(fax.value),
            'email': btoa(email_vcard.value),
            'company_ch': btoa(company.value),
            'job': btoa(job.value),
            'street': btoa(street.value),
            'city': btoa(city.value),
            'zip': btoa(zip.value),
            'state': btoa(state.value),
            'country': btoa(country.value),
            'website': btoa(website.value)
        }
    }
    //    console.log(JSON.stringify(send_vcard))
    reqapi(send_vcard)
}
// ============= funct text ========
function send_text() {
    let send_text = {
        'type': 'text',
        'data': {
            'content': btoa(text.value)
        }
    }
    //    console.log(JSON.stringify(send_text))
    reqapi(send_text)
}

// ==============funct email ===============
function send_email() {
    let send_email = {
        'type': 'email',
        'date': {
            'email': btoa(email_email.value),
            'subject': btoa(subject.value),
            'mess': btoa(mess.value)
        }
    }
    // console.log(JSON.stringify(send_email))
    reqapi(send_email)
}

// =============== funct network ============
ssid_hidden.addEventListener('change', hidden_ssid);
select_none.addEventListener('change', sel_none);
select_WPA_WPA2.addEventListener('change', sel_WPA_WPA2);
select_WEP.addEventListener('change', sel_WEP);

var hidden_par = 0;
var select_encryption = 'WPA/WPA2';
function hidden_ssid() {
    if (this.checked) {
        hidden_par = 1;
    } else {
        hidden_par = 0;
    }
}
function sel_none() {
    select_encryption = select_none.value;
}
function sel_WPA_WPA2() {
    select_encryption = select_WPA_WPA2.value;
}
function sel_WEP() {
    select_encryption = select_WEP.value;
}


function send_wifi() {
    let send_wifi = {
        'type': 'wifi',
        'data': {
            'network_name': btoa(network_name.value),
            'password': btoa(password.value),
            'encryption': btoa(select_encryption)
        }
    }
    // console.log(JSON.stringify(send_wifi));
    reqapi(send_wifi)
}

// ======== funct facebook ==========
function send_fb() {
    let send_fb = {
        'type': 'facebook',
        'data': {
            'url_facebook': btoa(url_fb.value),
            'name': btoa(name_fb.value),
            'title': btoa(title_fb.value),
            'website': btoa(website_fb.value)
        }
    }
    // console.log(JSON.stringify(send_fb))
    reqapi(send_fb)
}

// ========= func send req api =============
function reqapi(data) {
    document.getElementById('qr').src = '../resource/img/loading.gif';

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = () => {
        let qrcode = JSON.parse(xhttp.response);
        document.getElementById('qr').src = 'data:image/png;base64,' + qrcode['img'];
    }
    xhttp.open("POST", "http://139.162.46.99:8888/submit", true);
    xhttp.send(JSON.stringify(data));


}


