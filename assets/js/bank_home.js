


var search_btn = document.getElementById('btnsearch');
search_btn.onclick = function(){
    var  bloodclass,bloodtype, table, tr, td1, td2, i, txtValue1,txtValue2;
    bloodclass = document.getElementsByClassName("select1")[0].value;
    bloodtype = document.getElementsByClassName("select2")[0].value;

    filter1 = bloodclass.toUpperCase();//blood class
    filter2 = bloodtype.toUpperCase();// blood type

    table = document.getElementById("myTable");
    tr = table.getElementsByTagName("tr");
  
    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
      td1 = tr[i].getElementsByTagName("td")[1];//blood type
      td2 = tr[i].getElementsByTagName("td")[2];//blood class
      if (td1&&td2) {
        txtValue1 = (td1.textContent || td1.innerText);//blood type
        txtValue2 = (td2.textContent || td2.innerText);// bloodclass
     

        if ((txtValue1.toUpperCase().indexOf(filter2) > -1)&& (txtValue2.toUpperCase().indexOf(filter1)> -1)) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
}