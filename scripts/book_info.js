function displayBookInfoAndNavigate(bookName) {
    console.log("start", bookName);
    const writer_name = localStorage.getItem("login_username");
    localStorage.removeItem('book_name_last');
    localStorage.removeItem('current_chapter_id');
    showChapter(bookName);
    showComment(bookName);
    fetch(`/book/${bookName}?writer_name=${writer_name}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch book information');
            }
            return response.json();
        })
        .then(data => {
            console.log("message:" ,data.message);
            if (data.message == "This book is publishing or You are a writer"){
                sessionStorage.setItem('bookInfo', JSON.stringify(data));
                localStorage.setItem('book_name_last', bookName);
                console.log(localStorage.getItem('book_name_last'));
                console.log("book_name", bookName);
                window.location.href = "book_info.html";
            }
            else if (data.message == "This book is not publishing") {
                window.location.href = "book_hiding.html";
            }

        })
        .catch(error => {
            console.error('Error fetching book information:', error);
        });
}


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


const username = localStorage.getItem('login_username');
// console.log(username);
var data_chapter_id;


function NavigateToChapterInfo(chapter_id) {
    console.log("start");
    localStorage.removeItem('current_chapter_id');
    showComment(chapter_id);
    fetch(`/chapter/info/${chapter_id}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch chapter information');
            }
            console.log(response);
            return response.json();
        })
        .then(data => {
            sessionStorage.setItem('chapterInfo', JSON.stringify(data)); // Storing chapter info
            localStorage.setItem('current_chapter_id', chapter_id)
            console.log(chapter_id)

            check_bought_chapter(username, chapter_id)
                .then(is_chapter_bought => {
                    console.log(is_chapter_bought)
                    if ((data.cost && is_chapter_bought) || (data.cost == 0)){
                        go_to_chapter(); // Redirecting to another page
                    } else {
                        pop_up_buy_chapter(data);
                    }
                })
                .catch(error => {
                    console.error('Error checking if chapter is bought:', error);
                });
        })
        .catch(error => {
            console.error('Error fetching chapter information:', error);
        });
}

function go_to_chapter(){
    window.location.href = "reading_chapter.html";
}

function check_bought_chapter(username, chapter_id) {
    const url = `/check_bought_chapter/${username}?chapter_id=${chapter_id}`;
    return fetch(url, {
        method: 'GET',
        headers: { 'Content-Type': 'application/json' },
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Error');
        }
        return response.json();
    })
    .then(data => {
        console.log({data});
        return data;
    })
    .catch(error => {
        console.error('Error', error);
        throw error;
    });
}



function pop_up_buy_chapter(data) {
    var pop_up_element = document.getElementById('buy_chapter_pop_up');
    var pop_up_box = document.getElementById('buy_chapter_pop_up_box');

    pop_up_box.innerHTML = ''; // Clear the content of the pop-up
    var element = `
        <div class="buy_chapter_header">ซื้อตอน</div>
        <div onclick="close_pop_up_buy_chapter()" class="buy_chapter_cancel_button">
            <img src="../assets/writearead_img/close_button_light.png">
        </div>
        <hr class="lines"><br>
        <div class="pop_up_buy_chapter_name" id="buy_chapter_name">เรื่อง ${data.name}<br>ตอนที่ ${data.chapter_number}</div><br>
        <div onclick="buy_chapter()" class="buy_chapter_confirm_button" id="buy_chapter_button">ซื้อเลย ${data.cost} เหรียญ</div>
    `;
    pop_up_box.innerHTML = element;
    pop_up_element.style.display = 'block';
}


function close_pop_up_buy_chapter(){
    const pop_up_element = document.getElementById('buy_chapter_pop_up');
    pop_up_element.style.display = 'none';
}

function show_not_enough_coin() {
    get_coin_balance()
        .then(coinData => {
            var coin_balance = coinData.silver_coin + coinData.golden_coin;

            var pop_up_box = document.getElementById('buy_chapter_pop_up_box');
            pop_up_box.innerHTML = ''; // Clear the content of the pop-up

            var element = `
                <div class="buy_chapter_header">เติมคอยน์</div>
                <div onclick="close_pop_up_buy_chapter()" class="buy_chapter_cancel_button">
                    <img src="../assets/writearead_img/close_button_light.png">
                </div>
                <hr class="lines"><br>
                <div class="pop_up_buy_chapter_name" id="buy_chapter_name">
                    คุณมียอดคอยน์คงเหลือ <a style="color:var(--coin_color)">${coin_balance} coins</a><br>
                    ไม่เพียงพอในการซื้อครั้งนี้
                </div><br>
                <div onclick="go_to_buy_coin()" class="buy_chapter_confirm_button" id="buy_chapter_button">เติมคอยน์</div>
            `;

            pop_up_box.innerHTML = element;
        })
        .catch(error => {
            console.error('Error getting coin balance:', error);
        });
}

function show_purchased_successful() {
    get_coin_balance()
        .then(coinData => {
            var coin_balance = coinData.silver_coin + coinData.golden_coin;

            var pop_up_box = document.getElementById('buy_chapter_pop_up_box');
            pop_up_box.innerHTML = `
                <div class="buy_chapter_header">ซื้อตอน</div>
                <div onclick="close_pop_up_buy_chapter()" class="buy_chapter_cancel_button">
                    <img src="../assets/writearead_img/close_button_light.png">
                </div>
                <hr class="lines"><br>
                <div class="pop_up_buy_chapter_name" id="buy_chapter_name">
                    <a style="color:var(--main_color); font-size:16px"> ซื้อตอนสำเร็จ </a><br>
                    ยอดคงเหลือ <a style="color:var(--coin_color)">${coin_balance} coins</a>
                </div><br>
                <div onclick="go_to_chapter()" class="buy_chapter_confirm_button" style="background-color: var(--main_color_light);" id="buy_chapter_button">อ่านเลย</div>
            `;
        })
        .catch(error => {
            console.error('Error showing purchased successful:', error);
        });
}

function back_to_book_info() {
    console.log("back to book");
    displayBookInfoAndNavigate(localStorage.getItem('book_name_last'));
}

document.addEventListener('DOMContentLoaded', function () {
    const commentForm = document.getElementById('commentForm');
    const commentResponse = document.getElementById('comment_response');

    if (commentForm) {
        commentForm.addEventListener('submit', function (event) {
            event.preventDefault();
            
            const formData = new FormData(this);
            const jsonData = {};
            formData.forEach((value, key) => { jsonData[key] = value });
            jsonData.chapter_id = localStorage.getItem('current_chapter_id');
            jsonData.username = username;
            const jsonDataString = JSON.stringify(jsonData);

            console.log("new comment : ",jsonData);
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
    showComment(jsonData.chapter_id);

});


function buy_chapter() {
    const jsonData = {
        username: username,
        chapter_id: localStorage.getItem('current_chapter_id')
    };

    const jsonDataString = JSON.stringify(jsonData);

    fetch(`/buy_chapter/${username}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: jsonDataString
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Error');
        }
        return response.json();
    })
    .then(data => {
        console.log(data);
        if (data == 'Done') {
            show_purchased_successful();
        } else{
            show_not_enough_coin();
        }
    })
    .catch(error => {
        console.error('Error', error);
    })
}

function get_coin_balance(){
    return fetch(`/coin/${username}`, {
        method: 'GET',
        headers: { 'Content-Type': 'application/json' },
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Error');
        }
        return response.json();
    })
    .then(data => {
        console.log(data);
        return data;
    })
    .catch(error => {
        console.error('Error', error);
        throw error;
    });
}
