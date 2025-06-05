const map = L.map('map').setView([40.7128, -74.006], 13);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: 'Map data © OpenStreetMap contributors'
}).addTo(map);

const yearSlider = document.getElementById("yearSlider");
const selectedYear = document.getElementById("selectedYear");

yearSlider.addEventListener("input", async () => {
  const year = yearSlider.value;
  selectedYear.textContent = year;

  try {
    const response = await fetch(`/api/history?year=${year}`);
    const data = await response.json();

    const popup = L.popup()
      .setLatLng([40.7128, -74.006]) // New York City
      .setContent(`<b>Welcome to ${year}</b><br>${data.weather}<br>${data.event}`)
      .openOn(map);
  } catch (error) {
    console.error("Error fetching history data:", error);
  }
});

