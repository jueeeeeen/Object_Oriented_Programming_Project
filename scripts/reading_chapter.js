
const username = "Pangrum";
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

            current_chapter_id = chapter_id;
            console.log(current_chapter_id)

            // const username = localStorage.getItem('login_username');
            check_bought_chapter(username, chapter_id)
                .then(is_chapter_bought => {
                    console.log(is_chapter_bought)
                    if ((data.cost && is_chapter_bought) || (data.cost == 0)){
                        window.location.href = "reading_chapter.html"; // Redirecting to another page
                    } else {
                        pop_up_buy_chapter(data.cost);
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
        throw error; // Propagate the error to be caught in NavigateToChapterInfo
    });
}



function pop_up_buy_chapter(price){
    const pop_up_element = document.getElementById('buy_chapter_pop_up');
    const price_element = document.getElementById('buychapter')
    price_element.textContent = price + ' เหรียญ'
    price
    pop_up_element.style.display = 'block';
}

function close_pop_up_buy_chapter(){
    const pop_up_element = document.getElementById('buy_chapter_pop_up');
    pop_up_element.style.display = 'none';
}

function show_not_enough_coin(){
    const response_element = document.getElementById('purchase_response');
    response_element.textContent = 'เหรียญไม่พอ';
}

function show_purchased_successful(){
    const response_element = document.getElementById('purchase_response');
    response_element.textContent = 'ซื้อสำเร็จ';
}

function buy_chapter() {
    const jsonData = {
        username: username,
        chapter_id: current_chapter_id
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
        if (data === 'Done') {
            show_purchased_successful();
        } else {
            show_not_enough_coin();
        }
    })
    .catch(error => {
        console.error('Error', error);
    })
    .finally(() => {
        setTimeout(() => {
            close_pop_up_buy_chapter();
        }, 3000); // Adjust timeout as needed
    });
}
