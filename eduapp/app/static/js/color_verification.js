document.addEventListener("DOMContentLoaded", function() {
    const searchBox = document.getElementById('search-box');
    const resultsContainer = document.getElementById('results-container');

    searchBox.addEventListener('input', function() {
        const query = searchBox.value;

        fetch(`/api/search?q=${encodeURIComponent(query)}`)
            .then(response => response.json())
            .then(results => {
                resultsContainer.innerHTML = '';
                results.forEach(result => {
                    const item = document.createElement('div');
                    item.classList.add('result-item');
                    item.innerHTML = `
                        <h3>${result[0]}</h3>
                        <p>Size: ${result[1]}</p>
                        <p>Color: ${result[2]}</p>
                        <img src="${result[3]}" alt="${result[0]}">
                    `;
                    resultsContainer.appendChild(item);
                });
            })
            .catch(error => console.error("Error fetching search results:", error));
    });
});
