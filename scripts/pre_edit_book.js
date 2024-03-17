const writer_name = localStorage.getItem('login_username');

function displayPreEditBookAndNavigate(bookName) {
    console.log("start edit book");
    console.log("bookName : ",bookName);
    localStorage.removeItem('book_name_edit_last');
    localStorage.removeItem('chapter_id_last');
    showChapter(bookName);
    fetch(`/book/${bookName}?writer_name=${writer_name}`)
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to fetch book information');
        }
        return response.json();
    })
    .then(data => {
        sessionStorage.setItem('bookInfo', JSON.stringify(data));
        localStorage.setItem('book_name_edit_last', bookName);
        console.log("book_name_edit_last : ",localStorage.getItem('book_name_edit_last'));
        window.location.href = "pre_edit_book.html";
    })
    .catch(error => {
        console.error('Error fetching book information:', error);
    });
}

const book_name_edit_last = localStorage.getItem('book_name_edit_last');
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


function displayBookEditAndNavigate() {
    console.log("start");
    fetch(`/book/${book_name_edit_last}?writer_name=${writer_name}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch book information');
            }
            return response.json();
        })
        .then(data => {
            sessionStorage.setItem('bookInfo', JSON.stringify(data));
            window.location.href = "edit_book.html";
        })
        .catch(error => {
            console.error('Error fetching book information:', error);
        });
}

document.addEventListener('DOMContentLoaded', async function () {
    const editBookForm = document.getElementById('editBookForm');
    const responseDiv = document.getElementById('response');
    const old_genre = document.getElementById('old_genre');
    const old_name = document.getElementById('old_name');
    const old_name_input = document.getElementById('old_name_input');
    const old_pseudonym = document.getElementById('old_pseudonym');
    const old_age_restricted = document.getElementById('old_age_restricted');
    const old_status = document.getElementById('old_status');
    const old_prologue = document.getElementById('old_prologue');
    const old_date_time = document.getElementById('old_date_time');

    try {
        const response = await fetch(`/book/${book_name_edit_last}?writer_name=${writer_name}`);
        if (!response.ok) {
            throw new Error('Failed to fetch book information');
        }
        const bookData = await response.json();

        // Populate form fields with existing book information
        old_name.value = bookData.name;
        old_name_input.value = bookData.name;
        old_genre.value = bookData.genre;
        old_pseudonym.value = bookData.pseudonym;
        old_status.value = bookData.status;
        console.log("age_restricted",bookData.age_restricted)
        old_age_restricted.value = bookData.age_restricted;
        old_prologue.value = bookData.prologue;
        old_date_time.value = bookData.date_time;

    } catch (error) {
        console.error('Error fetching book information:', error);
    }

    if (editBookForm) {
        editBookForm.addEventListener('submit', async function (event) {
            event.preventDefault();
            try {
                const formData = new FormData(this);
                const jsonData = {};
                formData.forEach((value, key) => {
                    jsonData[key] = value;
                });
                
                console.log("start fetch book edit", jsonData.old_name);
                jsonData.writer_name = writer_name;

                const response = await fetch(`/edit_book`, { 
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(jsonData)
                });
    
                if (!response.ok) {
                    throw new Error('Failed to edit book');
                }
    
                const data = await response.json();
                if (response) {
                    responseDiv.innerText = data.message;
                }
    
                go_to_pre_edit_book();
            } catch (error) {
                console.error('Error editing book:', error);
            }
        });
    }
});
function go_to_pre_edit_book() {
    displayPreEditBookAndNavigate(book_name_edit_last);
}

function displayChapterEditAndNavigate(chapter_id) {
    console.log("chptre_id_last: ",chapter_id)
    localStorage.setItem('chapter_id_last', chapter_id)
    window.location.href = "edit_chapter.html";
}

document.addEventListener('DOMContentLoaded', async function () {
    const editChapterForm = document.getElementById('editChapterForm');
    const chapterIdInput = document.getElementById('chapter_id');
    const chapterNumberInput = document.getElementById('chapter_number');
    const nameInput = document.getElementById('name');
    const contextInput = document.getElementById('context');
    const costInput = document.getElementById('cost');
    console.log("chapter_id_last: ",localStorage.getItem('chapter_id_last'))

    try {
        const chapterId = localStorage.getItem('chapter_id_last'); 
        console.log(chapterId);
        const response = await fetch(`/chapter/info/${chapterId}`);
        if (!response.ok) {
            throw new Error('Failed to fetch chapter information');
        }
        const chapterData = await response.json();
        console.log("before chapterData: ", chapterData)
        // Populate form fields with existing chapter information
        chapterIdInput.value = chapterData.chapter_id;
        nameInput.value = chapterData.name;
        chapterNumberInput.value = chapterData.chapter_number
        contextInput.value = chapterData.context;
        costInput.value = chapterData.price;
    } catch (error) {
        console.error('Error fetching chapter information:', error);
    }

    if (editChapterForm) {
        editChapterForm.addEventListener('submit', async function (event) {
            event.preventDefault();

            try {
                const formData = new FormData(this);
                const jsonData = {};
                formData.forEach((value, key) => {
                    jsonData[key] = value;
                });
                console.log(jsonData);
                console.log("start post method");
                const response = await fetch('/edit_chapter', {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(jsonData)
                });

                if (!response.ok) {
                    throw new Error('Failed to edit chapter');
                }
                const data = await response.json();
                console.log("data after", data);
                if (response) {
                    console.log("data.value:", data.message)
                    response.innerText = data.message;
                }
                go_to_pre_edit_book();
            } catch (error) {
                console.error('Error editing chapter:', error);
            }
        });
    }
});