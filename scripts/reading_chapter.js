
const username = "Mozaza";
var data_chapter_id;

let current_chapter_id;

function NavigateToChapterInfo(chapter_id) {
    console.log("start");
    fetch(`/chapter/info/${chapter_id}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch chapter information');
            }
            console.log("receive response");
            return response.json();
        })
        .then(data => {
            sessionStorage.setItem('chapterInfo', JSON.stringify(data)); // Storing chapter info
            console.log(data);

            current_chapter_id = chapter_id;
            console.log(current_chapter_id)

            // const username = localStorage.getItem('login_username');
            const is_chapter_bought = check_bought_chapter(username, chapter_id);
            if ((data.cost && is_chapter_bought) || (data.cost == 0)){
                window.location.href = "reading_chapter.html"; // Redirecting to another page
            }else{
                pop_up_buy_chapter(username, chapter_id);
            }
        })
        .catch(error => {
            console.error('Error fetching chapter information:', error);
        });
}

function check_bought_chapter(username, chapter_id){
    const jsonData = {};
    jsonData['username'] = username;
    jsonData['chapter_id'] = chapter_id;
    console.log(jsonData);
    const jsonDataString = JSON.stringify(jsonData);
        fetch(`/check_bought_chapter/${username}`, {
            method: 'GET',
            headers: {'Content-Type': 'application/json'},
            body: jsonDataString
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Error');
                }
                return response.json();
            })
            .then(data => {
                return data;
            })
            .catch(error => {
                console.error('Error', error);
            });
        }

function pop_up_buy_chapter(){
    const pop_up_element = document.getElementById('buy_chapter_pop_up');
    pop_up_element.style.display = 'block';
}

function close_pop_up_buy_chapter(){
    const pop_up_element = document.getElementById('buy_chapter_pop_up');
    pop_up_element.style.display = 'none';
}

function show_not_enough_coin(){
    const pop_up_element = document.getElementById('buy_chapter_pop_up');
    pop_up_element.textContent = 'เหรียญไม่พอ';
}

function show_purchased_successful(){
    const pop_up_element = document.getElementById('buy_chapter_pop_up');
    pop_up_element.textContent = 'ซื้อสำเร็จ';
}

function buy_chapter(){

    const jsonData = {};
    jsonData['username'] = username;
    jsonData['chapter_id'] = current_chapter_id;
    
    console.log(jsonData);

    const jsonDataString = JSON.stringify(jsonData);
    

    fetch(`/buy_chapter/${username}`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
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
            setTimeout(() => {
                close_pop_up_buy_chapter();
            }, 3000);
        } else {
            show_not_enough_coin();
            setTimeout(() => {
                close_pop_up_buy_chapter();
            }, 3000);
        }
    })
    .catch(error => {
        console.error('Error', error);
    });
}