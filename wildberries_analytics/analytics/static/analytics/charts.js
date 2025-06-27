console.log("charts.js загружен");

async function loadData() {
    const min_price = document.getElementById("min_price").value;
    const min_rating = document.getElementById("min_rating").value;
    const min_feedbacks = document.getElementById("min_feedbacks").value;

    const params = new URLSearchParams({
        ...(min_price && {min_price}),
        ...(min_rating && {min_rating}),
        ...(min_feedbacks && {min_feedbacks})
    });

    const response = await fetch(`/api/products/?${params}`);
    const data = await response.json();

    const tbody = document.querySelector("#products_table tbody");
    tbody.innerHTML = '';
    data.forEach(item => {
        tbody.innerHTML += `
            <tr>
                <td>${item.name}</td>
                <td>${item.price}</td>
                <td>${item.sale_price}</td>
                <td>${item.rating}</td>
                <td>${item.feedbacks}</td>
            </tr>`;
    });

    drawCharts(data);
}

function drawCharts(data) {
    const prices = data.map(p => p.sale_price);
    const ratings = data.map(p => p.rating);
    const discounts = data.map(p => p.price - p.sale_price);

    if (window.priceChartInstance) window.priceChartInstance.destroy();
    if (window.discountRatingChartInstance) window.discountRatingChartInstance.destroy();

    window.priceChartInstance = new Chart(
        document.getElementById("priceHistogram"),
        {
            type: "bar",
            data: {
                labels: prices,
                datasets: [{
                    label: "Цены",
                    data: prices,
                    backgroundColor: "rgba(75,192,192,0.6)"
                }]
            }
        }
    );

    window.discountRatingChartInstance = new Chart(
        document.getElementById("discountVsRating"),
        {
            type: "line",
            data: {
                labels: ratings,
                datasets: [{
                    label: "Скидка vs Рейтинг",
                    data: discounts,
                    borderColor: "rgba(255,99,132,1)",
                    fill: false
                }]
            }
        }
    );
}

window.onload = loadData;
