// Fuction to color the elements according to their boolean
function colorElement(td, boolean) {
    if (boolean) {
        td.className = 'table-warning';

    }
    else {
        td.className = 'table-danger';
    }
}

// Making the database realtime
var db = firebase.firestore();
db.collection("users").doc("F3zKTfzFwe6ClSGXMKo7").collection("habits").orderBy("date", "desc").limit(10).onSnapshot(function(querySnapshot) {
    var new_tbody = document.createElement('tbody');
    new_tbody.setAttribute('id','habits');
    querySnapshot.forEach(function(doc) {
        // Insert new row
        var tr = new_tbody.insertRow();

        // Insert date
        var date = new Date(doc.data().date.seconds*1000);
        var td = tr.insertCell();
        td.appendChild(document.createTextNode(date.toDateString()));

        // Insert habits and modify class
        var td = tr.insertCell();
        colorElement(td, doc.data().no_snooze);

        var td = tr.insertCell();
        colorElement(td, doc.data().water_drank);

        var td = tr.insertCell();
        colorElement(td, doc.data().teeth_brushed_am);

        var td = tr.insertCell();
        colorElement(td, doc.data().no_www_used_am);

        var td = tr.insertCell();
        colorElement(td, doc.data().teeth_brushed_pm);

        var td = tr.insertCell();
        colorElement(td, doc.data().no_www_used_pm);

    });
    console.log(new_tbody);
    var old_tbody = document.getElementById('habits');
    old_tbody.parentNode.replaceChild(new_tbody, old_tbody);
});