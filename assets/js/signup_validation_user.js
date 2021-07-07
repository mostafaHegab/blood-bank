const email = document.getElementById('val-email');
const password = document.getElementById('val-pass');
const confirm1 = document.getElementById('val-confpass');
const names = document.getElementById('val-user');
const age = document.getElementById('val-age');

document.forms[1].onsubmit = (e) => {
    e.preventDefault();
 
    if (names.value < 6) {
        document.getElementById('validate-name').style.display = "block"
        return false;
    }
    else {
       document.getElementById('validate-name').style.display = "none"
    }

    let email_validation = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    if (!email.value.match(email_validation)) {
        document.getElementById('validate-email').style.display = "block"
         return false;

    }
    else {
       document.getElementById('validate-email').style.display = "none"
    }

    let passw= /^[a-zA-Z0-9!@#$%^&*]{6,25}$/;
    if (!password.value.match(passw)) {
        document.getElementById('validate-pass').style.display = "block"
    return false;
    }
    else {
       document.getElementById('validate-pass').style.display = "none"
    }



    if (confirm1.value != password.value){
      document.getElementById('pass-conf-validation').style.display = "block"
        return false;
    }
    else {
       document.getElementById('pass-conf-validation').style.display = "none"
    }

    let date = new Date();
    if (age.value == "") {
         document.getElementById('date-validate').style.display = "block"
        return false;
    }
    else if (parseInt(date.getUTCFullYear()) - parseInt(age.value.slice(0, 4)) < 18) {
      document.getElementById('date-validate').style.display = "block"
        return false;
    }
     else if (parseInt(date.getUTCFullYear()) - parseInt(age.value.slice(0, 4)) > 50) {
        document.getElementById('date-validate').style.display = "block"
        return false;
    }
    else {
       document.getElementById('date-validate').style.display = "none"
    }
    document.forms[1].submit();
}


// console.log(date.getUTCFullYear())

