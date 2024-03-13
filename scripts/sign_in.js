async function alert_success() {
    var username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const response = await axios.get(`http://127.0.0.1:8000/sign_in?username=${username}&password=${password}`)
    // var role = response.data.role;
    // console.log(response.data);
    console.log(response.data.response);
    console.log(response.data.role);
    if(password.length < 8) {
        alert('รหัสมากกว่า 8 ตัวอักษรขึ้นไปจ้า');
    } else {
        
        if(response.data.response == "log in successfully") {

            window.location.href = 'homepage.html';

            alert('เข้าสู่ระบบสำเร็จ!');
            localStorage.setItem('login_username', username);
            localStorage.setItem('login_role', response.data.role);

            console.log(localStorage.getItem('login_username'));
            console.log(localStorage.getItem('login_role'));

        } else if(response.data.response == "wrong password") {
            alert('เข้าสู่ระบบล้มเหลว! กรุณาตรวจสอบชื่อผู้ใช้และรหัสผ่านของคุณ');

        } else {
            alert('เกิดข้อผิดพลาด กรุณาลองใหม่อีกครั้ง');
        }
    }
    
}

