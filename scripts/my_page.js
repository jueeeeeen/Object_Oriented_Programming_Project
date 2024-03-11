var view_type = 0;

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


function select_type(num){
    view_type = num;
    $('#my_page_view_container').empty();
    var type = document.getElementsByClassName("my_page_view_type");
    for (let i = 0; i < type.length; i++) {
        type[i].style.borderBottom = "none";
    }
    type[view_type].style.borderBottom = "4px solid var(--main_color)";
    // show_type(current_data);
}


function show_type(current_data){
    $('#search_result_page').empty();
    if (search_type == 0){ //writing
        display_books();
    }
    else if(search_type == 1){ //pseudonym
        display_pseudonyms();
    }
    else{ //comments
        display_comments();
    }
}

function display_books(){

}

function display_pseudonyms(){

}

function display_not_found(){
    var element = not_found;
    $('#my_page_view_container').append(element);
}
