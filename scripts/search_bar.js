search_from_home();
function search_from_home(){
    document.addEventListener('DOMContentLoaded', (event) => {
        document.getElementById("searchForm").addEventListener("submit", function (e) {
            e.preventDefault();
            var search_str = document.getElementById('search_str').value;
            localStorage.setItem('search_str_from_home', search_str);
            window.location.href = 'search_page.html';
        });
    });
}