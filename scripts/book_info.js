// script.js

// Function to display book information and navigate
function displayBookInfoAndNavigate(bookName) {
    console.log("start");
    fetch(`/book/${bookName}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch book information');
            }
            return response.json();
        })
        .then(data => {
            sessionStorage.setItem('bookInfo', JSON.stringify(data));
            // showComment(bookName)
            // console.log("show comment")
            // showChapter(bookName)
            localStorage.setItem('book_name_last',bookName);
            console.log(localStorage.getItem('book_name_last'));
            window.location.href = "book_info.html";
        })
        .catch(error => {
            console.error('Error fetching book information:', error);
        });
}

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

document.addEventListener('DOMContentLoaded', function() {
    const commentForm = document.getElementById('commentForm');
    const commentResponse = document.getElementById('comment_response');

    if (commentForm) {
        commentForm.addEventListener('submit', function(event) {
            event.preventDefault();

            const formData = new FormData(this);
            const jsonData = {};
            formData.forEach((value, key) => { jsonData[key] = value });
            const jsonDataString = JSON.stringify(jsonData);

            fetch(`/comment/${jsonData.chapter_id}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: jsonDataString
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Failed to submit comment');
                }
                return response.json();
            })
            .then(data => {
                console.log("Submitted comment data:", data);
                if (commentResponse) {
                    commentResponse.innerText = JSON.stringify(data);
                }
                showComment(jsonData.chapter_id);
            })
            .catch(error => {
                console.error('Error submitting comment:', error);
            });
        });
    }

});

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
function back_to_book_info(){
    console.log("back to book")
    displayBookInfoAndNavigate(localStorage.getItem('book_name_last'))
}