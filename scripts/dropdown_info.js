function get_user_info{
    
}

function show_my_profile(){
    fetch('/my_profile/' + username, {
        method: 'GET',
    })
    .then(resp => resp.json())
    .then(data => {
        return
    })
    .catch(error => {
        console.error(error);
    });
}

function replace_dd_info{
    for (var key in current_data) {
        var element = document.getElementById('my_page_' + key);
        if (element) {
            var placeholder = '{' + key + '}';
            element.innerHTML = element.innerHTML.replace(placeholder, current_data[key]);
        }
    }
}