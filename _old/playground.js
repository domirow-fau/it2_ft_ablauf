function aktualisiere() {

    // var date = document.getElementById("date").value;
    var value = document.getElementById("value").value;
    // console.log(date);
    // console.log(value);
    d3.json("https://it2wi1.if-lab.de/rest/ft_ablauf")
        .then(function (data, error) {
            empfangeDaten(data, error, value);
        });
};

function empfangeDaten(datenEmpfangen, error, value) {
    // console.log(datenEmpfangen);
    if (error) {
        console.log(error);
    } else {
        zeigeDaten(datenEmpfangen, value);
    }
};

function zeigeDaten(daten, value) {

    console.log(daten[18].werte[value]);

    let buffer = [];

    for (var i = 0; i < Object.keys(daten).length - 1; i++) {
        if (daten[i].werte[value] != daten[i + 1].werte[value]) {
            buffer.push(daten[i + 1].datum);
        }
    };

    document.getElementById("statusChange").innerHTML = "Uhrzeiten, an denen sich was geaendert hat: \n" + JSON.stringify(buffer, null, 2);
    document.getElementById("numberstatusChange").innerHTML = "Number of status changes: " + buffer.length;

    p.exit().remove();


};