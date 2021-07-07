const last_treat_date = document.forms[0][0];
const last_donate_date = document.forms[0][3];
const weight = document.forms[0][1];

document.forms[0].onsubmit = (e) => {
    e.preventDefault();
    if (last_treat_date.value == "") {
        document.getElementById('ltdate').style.display = "block"
        return false;
    } else if (Math.floor((new Date() - new Date(document.forms[0][0].value))/86400000)< 14) {
        document.getElementById('ltdate').style.display = "block"
        return false;
    } else {
        document.getElementById('ltdate').style.display = "none"
    }

    if (weight.value == "") {
        document.getElementById('weights').style.display = "block"
    }
    else if (parseInt(weight.value) < 55) {
        document.getElementById('weights').style.display = "block"
     }
    else {
        document.getElementById('weights').style.display = "block"
    }

    
    if (last_donate_date.value == "") {
            document.getElementById('lddate').style.display = "block"
            return false;
        }
        else if (Math.floor((new Date() - new Date(document.forms[0][3].value))/(86400000*30)) < 6) {
        document.getElementById('lddate').style.display = "block"
            return false;
        }
        else {
        document.getElementById('lddate').style.display = "none"
    }
  
  document.forms[0].submit();
}