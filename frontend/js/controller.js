let butt_genergate_url = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type #butt_genergate_url');
let butt_genergate_vcard = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type #butt_genergate_vcard');
let butt_genergate_text = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type #butt_genergate_text');
let butt_genergate_email = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type #butt_genergate_email');
let butt_genergate_wifi = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type #butt_genergate_wifi');
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
let select_none = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type .container_input_row .col_chill label #select_none');
let select_WPA_WPA2 = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type .container_input_row .col_chill label #select_WPA_WPA2');
let select_WEP = document.querySelector('.home .container_left_input .container_menu_input_right .container_input_type .container_input_row .col_chill label #select_WEP');

let img_qr = document.querySelector('.home .container_right_output .container_img_qr #qr')

// ======== event genergate =========
butt_genergate_url.addEventListener('click', send_url);
// butt_genergate_url.addEventListener('click', get_Data);
butt_genergate_vcard.addEventListener('click', send_vcard);
butt_genergate_text.addEventListener('click', send_text);
butt_genergate_email.addEventListener('click', send_email);
butt_genergate_wifi.addEventListener('click', send_wifi);


// ======= funct url==============
function send_url() {
    let send_url = {
        'type': 'url',
        'data': {
            'content': b64encode(textarea_input.value),
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
            'fname': b64encode(first_name.value),
            'lname': b64encode(last_name.value),
            'mobile': b64encode(mobile.value),
            'phone': b64encode(phone.value),
            'fax': b64encode(fax.value),
            'email': b64encode(email_vcard.value),
            'company_ch': b64encode(company.value),
            'job': b64encode(job.value),
            'street': b64encode(street.value),
            'city': b64encode(city.value),
            'zip': b64encode(zip.value),
            'state': b64encode(state.value),
            'country': b64encode(country.value),
            'website': b64encode(website.value)
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
            'content': b64encode(text.value)
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
            'email': b64encode(email_email.value),
            'subject': b64encode(subject.value),
            'mess': b64encode(mess.value)
        }
    }
    // console.log(JSON.stringify(send_email))
    reqapi(send_email)
}

// =============== funct network ============
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
            'network_name': b64encode(network_name.value),
            'password': b64encode(password.value),
            'encryption': b64encode(select_encryption)
        }
    }
    // console.log(JSON.stringify(send_wifi));
    reqapi(send_wifi)
}

// ========= func send req api =============

function b64encode(text) {
    return window.btoa(unescape(encodeURIComponent(text)));
}

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


