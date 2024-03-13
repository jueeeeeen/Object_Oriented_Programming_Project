let toggle_dd_status = false;

function toggle_user_icon_drop_down(){
    toggle_search_off();
    toggle_dd_status = !toggle_dd_status;
    const dropdown = document.getElementById('home_dd_container');

    if (toggle_dd_status){
        dropdown.style.display = "block";
    }
    else{
        dropdown.style.display = "none";
    }
}

function go_to_my_page(){
    window.location.href = 'myPage.html';
}

function go_to_my_profile(){
    window.location.href = 'my_profile.html';
}

function go_to_buy_coin(){
    window.location.href = 'payment.html';
}

function go_to_my_reading(){
    window.location.href = 'my_reading.html';
}

function go_to_my_writing(){
    window.location.href = 'my_writing.html';
}

function go_to_my_coin_transac(){
    window.location.href = 'my_coin_tranasac.html';
}

function go_to_my_chapter_transac(){
    window.location.href = 'my_chapter_transac.html';
}

function go_to_homepage(){
    window.location.href = 'homepage.html';
}

function show_book_from_all(){
    document.addEventListener('DOMContentLoaded', (event) => {
        document.getElementById("searchFormPage").addEventListener("submit", function (e) {
            e.preventDefault(); // Cancel the default action
            var search_str = document.getElementById('searchInputPage').value;
            fetch('/search_all/' + search_str, {
                method: 'GET',
            })
            .then(resp => resp.json())
            .then(data => {
                current_data = data;
                $('#search_result_page').empty();
                show_type(data);
            })
            .catch(error => {
                console.error(error);
            });
        });
    });
}