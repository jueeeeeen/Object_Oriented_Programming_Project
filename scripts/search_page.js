document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById("searchFormPage").addEventListener("submit", function (e) {
        e.preventDefault(); // Cancel the default action
        var search_str = document.getElementById('searchInputPage').value;
        fetch('/search_all/' + search_str, {
            method: 'GET',
        })
        .then(resp => resp.json())
        .then(data => {
            $('#search_result').empty();
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
    $('#search_result_page').append('<h3>' + category + ' :</h3>');
    if (Array.isArray(results)) {
        results.forEach(result => {
            $('#search_result_page').append('<ul>' + result + '</ul>');
        });
    } else {
        $('#search_result_page').append('<ul>' + results + '</ul>');
    }
}
