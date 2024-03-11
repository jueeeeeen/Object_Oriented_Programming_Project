search();

var receivedString = getParams().data;
console.log('Received Data:', receivedString);

{/* <div class="search_result_container">
                <div class="image-container">
                    <img src="../assets/covers_img/temp_cover.jpg" alt="Book Cover">
                </div>
                <div class="book_content_container"><br>
                    <p class="title">ปีที่แล้วเธอกับฉันเราพลัดหลงกัน</p>
                    <p class="description">นามปากกา</p>
                    <p class="description">หมวดหมู่</p>
                    <p class="description">อื่นๆ</p>
                </div>
            </div> */}

const search_result_container = document.createElement()

const search_result = '<div class="search_result_container"></div>'
search_result.innerhtml = '<p class="title">ปีที่แล้วเธอกับฉันเราพลัดหลงกัน</p>'
const open_tag = '<div class="search_result_container"><div class="image-container"><img src="image/temp_cover.jpg" alt="Book Cover"></div><div class="book_content_container"><br><p class="title">'
const close_tag = '</p><p class="description">นามปากกา</p><p class="description">หมวดหมู่</p><p class="description">อื่นๆ</p></div></div>'

const not_found = '<a class="not_found">ไม่พบรายการค้นหา</a>'

if (receivedString){
    search_by_string(receivedString);
}

var current_data; 
var search_type = 0;

function select_type(num){
    search_type = num;
    var type = document.getElementsByClassName("search_type");
    for (let i = 0; i < type.length; i++) {
        type[i].style.borderBottom = "none";
    }
    type[search_type].style.borderBottom = "4px solid var(--main_color)";
    show_type(current_data);
}

function show_type(current_data){
    $('#search_result_page').empty();
    if (search_type == 0){
        display_all(current_data);
    }
    else if(search_type == 1){
        display_books();
    }
    else{
        display_pseudonyms();
    }
}

function search(){
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

function search_by_string(search_str){
            fetch('/search_all/' + search_str, {
                method: 'GET',
            })
            .then(resp => resp.json())
            .then(data => {
                const search_input = document.getElementById("searchInputPage")
                search_input.value = search_str;
                current_data = data;
                $('#search_result_page').empty();
                show_type(data);
            })
            .catch(error => {
                console.error(error);
            });
}

function display_books(){
    if (current_data.book.length == 0) {
        display_not_found();
    }
    else{
        current_data.book.forEach(result => {
            var element = open_tag + result + close_tag;
            $('#search_result_page').append(element);
        });
    }   
}

function display_pseudonyms(){
    if (current_data.pseudonym.length == 0) {
        display_not_found();
    }
    else{
        current_data.pseudonym.forEach(result => {
            var element = open_tag + result + close_tag;
            $('#search_result_page').append(element);
        });
        console.log(not_found);
    }   
}

function display_not_found(){
    var element = not_found;
    $('#search_result_page').append(element);
}

function display_all(results) {
    if (results.book.length == 0 && results.pseudonym.length == 0) {
        display_not_found();
    } else {
        if (results.book.length != 0) {
            results.book.forEach(result => {
                var element = open_tag + result + close_tag;
                $('#search_result_page').append(element);
            });
        }
        if (results.pseudonym.length != 0) {
            results.pseudonym.forEach(result => {
                var element = open_tag + result + close_tag;
                $('#search_result_page').append(element);
            });
        }
    }
}


function getParams() {
    var params = {};
    var paramArray = window.location.search.substring(1).split('&');

    for (var i = 0; i < paramArray.length; i++) {
        var pair = paramArray[i].split('=');
        params[pair[0]] = decodeURIComponent(pair[1]);
    }

    return params;
}

