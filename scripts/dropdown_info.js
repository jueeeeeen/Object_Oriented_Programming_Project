var username = localStorage.getItem('login_username')

function get_user_info() {
    return Promise.all([get_coin_balance(), get_my_profile()])
        .then(([coinData, profileData]) => {
            var display_name = profileData.display_name;
            var username = localStorage.getItem('login_username');
            var golden_coin = coinData.golden_coin;
            var silver_coin = coinData.silver_coin;

            var total_coin = golden_coin + silver_coin;

            return {
                display_name: display_name,
                username: username,
                golden_coin: golden_coin,
                silver_coin: silver_coin,
                total_coin: total_coin
            };
        })
        .catch(error => {
            console.error('Error getting user info:', error);
            throw error; // Rethrow the error to reject the promise
        });
}


function get_my_profile() {
    return fetch('/my_profile/' + username, {
        method: 'GET',
        headers: { 'Content-Type': 'application/json' },
    })
    .then(resp => {
        if (!resp.ok) {
            throw new Error('Failed to fetch profile data');
        }
        return resp.json();
    })
    .catch(error => {
        console.error('Error fetching profile data:', error);
        throw error;
    });
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
        return data;
    })
    .catch(error => {
        console.error('Error', error);
        throw error;
    });
}

function replace_dd_info() {
    get_user_info().then(user_info => {
        for (var key in user_info) {
            var element = document.getElementById('dd_' + key);
            if (element) {
                var placeholder = '{' + key + '}';
                element.innerHTML = element.innerHTML.replace(placeholder, user_info[key]);
            }
        }
    }).catch(error => {
        console.error('Error replacing dropdown info:', error);
    });
}
