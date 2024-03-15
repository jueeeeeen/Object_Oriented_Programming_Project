// script.js
// book_display_img();

// Function to display book information and navigate
function displayBookInfoAndNavigate(bookName) {
    console.log("start",bookName);
    fetch(`/book/${bookName}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch book information');
            }
            return response.json();
        })
        .then(data => {
            sessionStorage.setItem('bookInfo', JSON.stringify(data));
            localStorage.setItem('book_name_last', bookName);
            console.log(localStorage.getItem('book_name_last'));
            console.log("book_namee",bookName)
            window.location.href = "book_info.html";
        })
        .catch(error => {
            console.error('Error fetching book information:', error);
        });
}

// function book_display_img() {
//     console.log("book-name_display",localStorage.getItem('book_name_last'))
//     var book_name = localStorage.getItem('book_name_last');
//     var book_img_element = `<img class="book_cover" src="assets/cover_img/${book_name}.png" alt="book_pic">`;
//     $('#book_display_img').html(book_img_element);
// }


// Function to fetch and display comments
function showComment(chapter_id) {
    console.log(`Fetching comments for chapter ${chapter_id}...`);
    fetch(`/chapter/comment/${chapter_id}`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Failed to fetch comments for chapter ${chapter_id}`);
            }
            return response.json();
        })
        .then(data => {
            console.log(`Received comments for chapter ${chapter_id}:`, data);
            // Store the comment data in sessionStorage
            sessionStorage.setItem('commentData', JSON.stringify(data));
        })
        .catch(error => {
            console.error('Error fetching comments:', error);
        });
}

function showChapter(book_name) {
    console.log(`Fetching chapter for book ${book_name}...`);
    fetch(`/book/chapter/${book_name}`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Failed to fetch chapter for chapter ${book_name}`);
            }
            return response.json();
        })
        .then(data => {
            console.log(`Received chapter for book ${book_name}:`, data);
            sessionStorage.setItem('chapterData', JSON.stringify(data));
        })
        .catch(error => {
            console.error('Error fetching chapters:', error);
        });
}

