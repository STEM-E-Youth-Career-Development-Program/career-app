async function fetchBLSData() {
  const url = '/bls-data';
  
  try {
    const response = await fetch(url);
    const seriesData = await response.json();

    if (seriesData && Array.isArray(seriesData)) {
      displayData(seriesData);
    } else {
      console.error("No data found in BLS response.");
    }
  } catch (error) {
    console.error("Error fetching data from Flask endpoint:", error);
  }
}

function displayData(seriesData) {
  const container = document.querySelector(".content-container");
  const dataElement = document.createElement("div");

  dataElement.innerHTML = `<h3>Latest BLS Data</h3>`;

  seriesData.forEach((item) => {
    const entry = document.createElement("p");
    entry.textContent = `Year: ${item.year}, Month: ${item.periodName}, Value: ${item.value}`;
    dataElement.appendChild(entry);
  });

  container.appendChild(dataElement);
}

// Call the function when the page loads
document.addEventListener("DOMContentLoaded", fetchBLSData);
