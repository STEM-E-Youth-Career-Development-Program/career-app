

const apiKey = '3d92d94931795cle125e3229b4ad7efc'; // FRED API Key
const endpoint = 'https://api.stlouisfed.org/fred/series/observations';
const seriesId = 'U.S. GDP'; 

async function fetchEconomicData() {
  try {
    const response = await fetch(
      `${endpoint}?series_id=${seriesId}&api_key=${apiKey}&file_type=json`
    );
    const data = await response.json();
    displayData(data);
  } catch (error) {
    document.getElementById('economic-data').innerHTML = '<p>Error loading data.</p>';
    console.error('Error fetching FRED data:', error);
  }
}

function displayData(data) {
  const observations = data.observations.slice(-5); // Get the latest 5 observations
  let content = '<h3>Latest Economic Data (GDP)</h3><ul>';
  observations.forEach(obs => {
    content += `<li>${obs.date}: $${parseFloat(obs.value).toFixed(2)} Billion</li>`;
  });
  content += '</ul>';

  document.getElementById('economic-data').innerHTML = content;
}

// Fetch data on page load
document.addEventListener('DOMContentLoaded', fetchEconomicData);
