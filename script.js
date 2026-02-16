function getCrops() {
    let soil = document.getElementById("soil").value;

    fetch("/recommend", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ soil: soil })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("cropResult").innerText =
            "Recommended Crops: " + data.crops.join(", ");
    });
}

function getPest() {
    let crop = document.getElementById("cropName").value;

    fetch("/pest", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ crop: crop })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("pestResult").innerText =
            "Pest Info: " + data.pest;
    });
}

function calculateProfit() {
    let area = document.getElementById("area").value;
    let yield_amt = document.getElementById("yield").value;
    let price = document.getElementById("price").value;

    fetch("/profit", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ area: area, yield: yield_amt, price: price })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("profitResult").innerText =
            `Revenue: ₹${data.revenue} | Cost: ₹${data.cost} | Profit: ₹${data.profit}`;
    });
}
