// my_writing_show_my_writings();

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('addChapterButton').addEventListener('click', function() {
        window.location.href = "create_chapter.html"; 
    });

    function displayPreEditChapterAndNavigate(bookName) {
        console.log("start");

        fetch(`/book/${bookName}`)
            .then(response => response.json())
            .then(data => {
                console.log("oooo")
                sessionStorage.setItem('PreEditChapter', JSON.stringify(data));

                const PreEditChapter = JSON.parse(sessionStorage.getItem('PreEditChapter'));

                console.log("Retrieved book information:", data);

                if (PreEditChapter && PreEditChapter.genre && PreEditChapter.name && PreEditChapter.pseudonym && PreEditChapter.prologue && PreEditChapter.writer_name && bookInfo.date_time) {

                    document.getElementById('genre').textContent = PreEditChapter.genre;
                    document.getElementById('bookName').textContent = PreEditChapter.name;
                    document.getElementById('prologueInfo').textContent = PreEditChapter.prologue;
                    document.getElementById('prologueDisplay').textContent = PreEditChapter.prologue;
                    document.getElementById('pseudonymInfo').textContent = PreEditChapter.pseudonym;
                    document.getElementById('pseudonymDisplay').textContent = PreEditChapter.pseudonym;
                    document.getElementById('writer_username').textContent = PreEditChapter.writer_name;
                    document.getElementById('date_time').textContent = PreEditChapter.date_time;
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }
});

function my_writing_show_my_writings(){
    let my_writings = localStorage.getItem('my_page_data').my_writings;
    $('#my_writing_show_result').empty(); // Remove existing data
    console.log(my_writings);
    my_writings.forEach(result => {
        var book_name = result.book_name;
        var pseudonym = result.pseudonym;
        var genre = result.genre;
        var element = `<div class="my_writing_writing_container">
                            <div class="my_writing_image_container" onclick="displayPreEditChapterAndNavigate('${book_name}')">
                                <img src="../assets/covers_img/${book_name}.jpg" alt="Book Cover">
                            </div>
                            <div class="my_writingbook_content_container" onclick="displayPreEditChapterAndNavigate('${book_name}')"><br>
                                <p class="my_writing_book_title">${book_name}</p>
                                <p class="my_writing_book_description">${pseudonym}</p>
                                <p class="my_writing_book_description">${genre}</p>
                            </div>
                        </div>`;
        $('#my_writing_show_result').append(element); 
    });
}