var view_type = 0;
let current_data;
let search_type = 0;


const username = localStorage.getItem('login_username');
// const username = "Mozaza";

show_my_page();

const not_found_html = '<a class="not_found">ไม่พบข้อมูล</a>'
const pseudonym_html = '<a class="not_found">นามปากกา</a>'
const show_book_html = `<div class="search_result_container">
                        <div class="image-container">
                            <img src="../assets/covers_img/${book_name}.png" alt="../assets/covers_img/temp_cover.jpg">
                        </div>
                        <div class="book_content_container"><br>
                            <p class="book_title">${book_name}</p>
                            <p class="book_description">${pseudonym}</p>
                            <p class="book_description">${genre}</p>
                        </div>
                    </div>`;

function my_page_select_view_type(num){
    search_type = num;
    var view_type = document.getElementsByClassName("my_page_view_type");
    for (let i = 0; i < view_type.length; i++) {
        view_type[i].style.borderBottom = "none";
    }
    view_type[search_type].style.borderBottom = "4px solid var(--main_color)";
    my_page_show_type();
}

function my_page_show_type(){
    if (search_type == 0){
        display_writings();
    }
    else{
        display_pseudonym();
    }
}

function show_my_page(){
            fetch('/my_page/' + username, {
                method: 'GET',
            })
            .then(resp => resp.json())
            .then(data => {
                console.log(data);
                current_data = data;
                display_img();
                display_my_page();
                display_writings();
            })
            .catch(error => {
                console.error(error);
            });
}

function display_img() {    
    // Create the HTML string for the profile image
    var profile_img_element = `<img class="profile_pic" src="../assets/profile_img/${username}.png" alt="profile_pic" onerror="this.onerror=null;this.src='../assets/header_img/user_button_light.png';" 
    alt="../assets/header_img/user_button_light.png">`;

    // Replace the content of the existing container with the new HTML
    $('#profile_pic_container').html(profile_img_element);
}

function display_my_page(){
    for (var key in current_data) {
        var element = document.getElementById('my_page_' + key);
        if (element) {
            var placeholder = '{' + key + '}';
            element.innerHTML = element.innerHTML.replace(placeholder, current_data[key]);
        }
    }
}

function display_writings() {
    $('#my_page_show_result').empty(); // Remove existing data
    current_data.writings.forEach(result => {
        display_writing_result(result);
    });
}

function display_pseudonym() {
    $('#my_page_show_result').empty(); // Remove existing data
    current_data.pseudonyms.forEach(pseudonym => {
        var pseudonym_element = `<div class="my_page_pseudonym_box">${pseudonym}</div>`;
        $('#my_page_show_result').append(pseudonym_element);
    });
}

function display_writing_result(result){
    var book_name = result.book_name;
    var pseudonym = result.pseudonym;
    var genre = result.genre;
    var element = `<div class="search_result_container">
    <div class="image-container">
        <img src="../assets/covers_img/${book_name}.png" 
            onerror="this.onerror=null;this.src='../assets/covers_img/temp_cover.jpg';" 
            alt="../assets/covers_img/temp_cover.jpg">
    </div>
    <div class="book_content_container"><br>
        <p class="book_title">${book_name}</p>
        <p class="book_description">${pseudonym}</p>
        <p class="book_description">${genre}</p>
    </div>
</div>`;
    $('#my_page_show_result').append(element);
}