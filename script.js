let cities = [];

function addCity() {
    let cityInput = document.getElementById('city-input');
    let city = cityInput.value.trim();
    if (city && !cities.includes(city)) {
        cities.push(city)
        let cityList = document.getElementById('city-list');
        let li = document.createElement('li')
        li.textContent = city;
        cityList.appendChild(li)
    }
    cityInput.value = '';
}