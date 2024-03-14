//show_all_book
show_all_book();
function show_all_book(){
    fetch('/show_all_book', {
        method: 'GET',
    })
    .then(resp => resp.json())
    .then(data => {
        console.log(data);
        $('#home_page_book_flexbox').empty();
        data.forEach(writing => {
            home_display_writing(writing);
        });
    })
    .catch(error => {
        console.error(error);
    });
}

function home_display_writing(writing) {
    console.log(writing.book_name);
    var element = `<div class="homepage_book_item">
                        <div class="homepage_cover_container" onclick="displayBookInfoAndNavigate('${writing.book_name}')" ><img src="../assets/covers_img/${writing.book_name}.png"></div>
                        <a class="homepage_book_title" onclick="displayBookInfoAndNavigate('${writing.book_name}')">${writing.book_name}</a>
                        <a class="homepage_book_pseudonym">${writing.pseudonym}</a>
                    </div>`;
    $('#home_page_book_flexbox').append(element);
    };