let current_data;

username = localStorage.getItem('login_username');
// const username = "Mozaza"

show_my_profile();

function my_page_select_view_type(num){
    search_type = num;
    var view_type = document.getElementsByClassName("my_page_view_type");
    for (let i = 0; i < view_type.length; i++) {
        view_type[i].style.borderBottom = "none";
    }
    view_type[search_type].style.borderBottom = "4px solid var(--main_color)";
    my_page_show_type();
}

// ชั่วคราววว
function show_my_profile(){
            fetch('/my_profile/' + username, {
                method: 'GET',
            })
            .then(resp => resp.json())
            .then(data => {
                current_data = data;
                my_profile_display_img();
                display_my_profile();
            })
            .catch(error => {
                console.error(error);
            });
}

function my_profile_display_img() {
    console.log(current_data);
    var username = current_data.username;
    var profile_img_element = `<img class="my_profile_profile_pic" src="../assets/profile_img/${username}.png" alt="profile_pic" onerror="this.onerror=null;this.src='../assets/header_img/user_button_light.png';" 
    alt="../assets/header_img/user_button_light.png">`

    $('#my_profile_profile_pic_container').html(profile_img_element);
}

function display_my_profile(){
    var name_element = document.getElementById('my_profile_display_name');
    name_element.textContent = current_data.display_name;
    var pic_element = document.getElementById('my_profile_username');
    pic_element.textContent = current_data.username;
}

document.addEventListener('DOMContentLoaded', function() {
    const change_password_form = document.getElementById('change_password_form');
    const response_text = document.getElementById('response_change_password')
    console.log(change_password_form);
    if (change_password_form) {
        change_password_form.addEventListener('submit', function(event) {
            event.preventDefault();
            
            const formData = new FormData(this);
            const jsonData = {};
            
            jsonData['username'] = username;
            
            console.log(jsonData);
            formData.forEach((value, key) => { jsonData[key] = value 
                console.log('added')});

            const jsonDataString = JSON.stringify(jsonData);
            
            fetch(`/change_password/${username}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: jsonDataString
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Failed to change password');
                }
                return response.json();
            })
            .then(data => {
                console.log(data);
                if (data == 'Done'){
                    response_text.textContent = 'เปลี่ยนรหัสผ่านแล้ว'
                    response_text.style.display = 'block'
                }
                else if(data == "Wrong"){
                    response_text.textContent = 'รหัสผ่านผิด'
                    response_text.style.display = 'block'
                }
                else if(data == "Length"){
                    response_text.textContent = 'เปลี่ยนรหัสผ่านแล้ว'
                    response_text.style.display = 'block'   
                }
            })
            .catch(error => {
                console.error('Error changing password:', error);
            });
        });
    }
});


function toggle_change_password() {
    const change_password_box = document.getElementById("my_profile_change_password")

    change_password_box.style.display = "block";
}

function toggle_change_password_off(){
    var change_password_box = document.getElementById("my_profile_change_password")

    change_password_box.style.display = "none";
}
