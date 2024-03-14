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
    window.location.href = 'my_page.html';
}

function go_to_my_profile(){
    window.location.href = 'my_profile.html';
}

function go_to_buy_coin(){
    window.location.href = 'payment.html';
}

function go_to_my_writing(){
    window.location.href = 'my_writing.html';
}

function go_to_transac(){
    window.location.href = 'transaction.html';
}

function go_to_homepage(){
    window.location.href = 'homepage.html';
}

function go_to_create_book(){
    window.location.href = "../Templates/create_book.html";
}

function go_to_create_chapter(){
    window.location.href = "../Templates/create_chapter.html";
}

function go_to_sign_in(){
    localStorage.removeItem('login_username')
    window.location.href = '../Templates/sign_in.html'
}