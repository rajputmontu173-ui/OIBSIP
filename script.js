// ==============================
// Airline Delay Dashboard
// script.js
// ==============================

let allData = [];

let barChart = null;
let pieChart = null;

// ==============================
// Load CSV
// ==============================

function loadData() {

    fetch("data.csv")

    .then(response => response.text())

    .then(csv => {

        let rows = csv.trim().split("\n");

        allData = [];

        for (let i = 1; i < rows.length; i++) {

            let cols = rows[i].split(",");

            allData.push({

                flight: cols[0],

                airline: cols[1],

                origin: cols[2],

                destination: cols[3],

                delay: Number(cols[4])

            });

        }

        showTable(allData);

        updateStatistics(allData);

        createCharts(allData);

    });

}

// ==============================
// Show Table
// ==============================

function showTable(data){

    let tbody = document.querySelector("#table tbody");

    tbody.innerHTML="";

    data.forEach(item=>{

        let tr=document.createElement("tr");

        let status="On Time";

        let cls="low";

        if(item.delay>30){

            status="Delayed";

            cls="high";

        }

        else if(item.delay>=10){

            status="Normal";

            cls="medium";

        }

        tr.className=cls;

        tr.innerHTML=`

        <td>${item.flight}</td>

        <td>${item.airline}</td>

        <td>${item.origin}</td>

        <td>${item.destination}</td>

        <td>${item.delay}</td>

        <td>${status}</td>

        `;

        tbody.appendChild(tr);

    });

}

// ==============================
// Statistics
// ==============================

function updateStatistics(data){

    document.getElementById("totalFlights").innerHTML=data.length;

    let delays=data.map(d=>d.delay);

    let total=delays.reduce((a,b)=>a+b,0);

    let avg=(total/data.length).toFixed(1);

    let max=Math.max(...delays);

    let min=Math.min(...delays);

    document.getElementById("avgDelay").innerHTML=avg;

    document.getElementById("maxDelay").innerHTML=max;

    document.getElementById("minDelay").innerHTML=min;

}

// ==============================
// Search Airline
// ==============================

function searchFlight(){

    let text=document.getElementById("search").value.toLowerCase();

    let filtered=allData.filter(item=>

        item.airline.toLowerCase().includes(text)

    );

    showTable(filtered);

    updateStatistics(filtered.length ? filtered : allData);

}

// ==============================
// Dark Mode
// ==============================

function toggleDarkMode(){

    document.body.classList.toggle("dark");

}

// ==============================
// Download Report
// ==============================

function downloadReport(){

    let report="Airline Delay Report\n\n";

    allData.forEach(item=>{

        report+=`${item.flight} | ${item.airline} | ${item.delay} Minutes\n`;

    });

    let blob=new Blob([report],{type:"text/plain"});

    let a=document.createElement("a");

    a.href=URL.createObjectURL(blob);

    a.download="Airline_Report.txt";

    a.click();

}

// ==============================
// Charts
// ==============================

function createCharts(data){

    let labels=data.map(d=>d.airline);

    let delays=data.map(d=>d.delay);

    if(barChart){

        barChart.destroy();

    }

    if(pieChart){

        pieChart.destroy();

    }

    barChart=new Chart(

        document.getElementById("barChart"),

        {

            type:"bar",

            data:{

                labels:labels,

                datasets:[{

                    label:"Delay",

                    data:delays

                }]

            }

        }

    );

    pieChart=new Chart(

        document.getElementById("pieChart"),

        {

            type:"pie",

            data:{

                labels:labels,

                datasets:[{

                    data:delays

                }]

            }

        }

    );

}