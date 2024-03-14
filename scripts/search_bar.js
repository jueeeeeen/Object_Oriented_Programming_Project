search_from_home();

function toggle_search() {
    const searchBar = document.getElementById("searchBar")
    const searchInput = document.getElementById("search_str")

    searchBar.style.display = "flex";
    searchInput.focus();
    
}

function toggle_search_off(){
    var searchBar = document.getElementById("searchBar")

    console.log(searchBar)

    searchBar.style.display = "none";
}

function search_from_home(){
    document.addEventListener('DOMContentLoaded', (event) => {
        document.getElementById("searchForm").addEventListener("submit", function (e) {
            e.preventDefault();
            var search_str = document.getElementById('search_str').value;
            sessionStorage.setItem('search_str_from_home', search_str);
            window.location.href = 'search_page.html';
        });
    });
}