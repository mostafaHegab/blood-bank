/** @format */

const refuse = document.getElementById("refuse");

refuse.addEventListener("click", () => {
    document.getElementById("hasDis").removeAttribute("disabled");
    document.getElementById("weight").removeAttribute("disabled");
    document.getElementById("refuse").classList.add("d-none");
    document.getElementById("ref").classList.remove("d-none");
});
