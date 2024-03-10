document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById("searchForm").addEventListener("submit", function (e) {
        e.preventDefault(); // Cancel the default action
        var search_str = document.getElementById('search_str').value;
        fetch('/search_all/' + search_str, {
            method: 'GET',
        })
        .then(resp => resp.json())
        .then(data => {
            $('#search_result').empty();
            toggle_search_off();
            displayResults('Reader', data.Search.Reader);
            displayResults('Writer', data.Search.Writer);
            displayResults('Book', data.Search.Book);
        })
        .catch(error => {
            console.error(error);
        });
    });
});

function displayResults(category, results) {
    $('#search_result').append('<h3>' + category + ' :</h3>');
    if (Array.isArray(results)) {
        results.forEach(result => {
            $('#search_result').append('<ul>' + result + '</ul>');
        });
    } else {
        $('#search_result').append('<ul>' + results + '</ul>');
    }
}
