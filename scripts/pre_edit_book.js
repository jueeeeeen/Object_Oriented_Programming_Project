// script.js
// book_display_img();
// Function to display book information and navigate

function displayPreEditBookAndNavigate(bookName) {
    console.log("start edit book");
    console.log("bookName : ",bookName)
    fetch(`/book/${bookName}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch book information');
            }
            return response.json();
        })
        .then(data => {
            sessionStorage.setItem('bookInfo', JSON.stringify(data));
            localStorage.setItem('book_name_edit_last', bookName);
            console.log(localStorage.getItem('book_name_edit_last'));
            console.log("book_namee",bookName)
            window.location.href = "pre_edit_book.html";
        })
        .catch(error => {
            console.error('Error fetching book information:', error);
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

function back_to_book_info() {
    console.log("back to book")
    displayBookInfoAndNavigate(localStorage.getItem('book_name_edit_last'))
}