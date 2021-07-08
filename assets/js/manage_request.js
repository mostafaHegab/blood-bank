/** @format */

console.log('hello')

let select = document.getElementsByTagName('select')[0];
let amount = document.getElementById('amount');

function getAc() {}

document.forms[0].onsubmit = (e) => {
	e.preventDefault();
	var opt;
	var count = 0;
	for (var i = 0, len = select.options.length; i < len; i++) {
		opt = select.options[i];
		if (opt.selected === true) {
			// console.log(opt.value);
			count++;
		}
	}
	// console.log(count);

	if (parseInt(amount.textContent) < count || count == 0) {
		document.getElementById('count-validate').style.display = 'block';
		return false;
	} else {
		document.getElementById('count-validate').style.display = 'none';
	}
	document.forms[0].submit();
};
