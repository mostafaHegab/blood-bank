const last_treat_date = document.forms[0][0];
const last_donate_date = document.forms[0][3];

document.forms[0].onsubmit = (e) => {
    e.preventDefault();
    let date = new Date();
    if (last_donate_date.value == "") {
            document.getElementById('date-validate').style.display = "block"
            return false;
        }
        else if (parseInt(date.getMonth()) - parseInt(last_donate_date.value.slice(5, 7)) < 6) {
        document.getElementById('ldd-validate').style.display = "block"
            return false;
        }
        else {
        document.getElementById('date-validate').style.display = "none"
    }
    

    let alldays = parseInt(date.value.slice(5, 7)) * 30 + parseInt(date.value.slice(8, 11));
    let compdays = date.getMonth() * 30 + date.getDay();
    if (last_treat_date.value == "") {
        document.getElementById('date-validate').style.display = "block"
        return false;
    } else if (compdays - alldays < 14) {
        document.getElementById('ldd-validate').style.display = "block"
        return false;
    } else {
        document.getElementById('date-validate').style.display = "none"
    }
  document.forms[1].submit();
}