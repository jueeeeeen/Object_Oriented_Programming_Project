var role = '';


document.getElementById('role').addEventListener('change', function() {
    role = this.value;
});


async function alert_success() {
    var username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const birth_date = document.getElementById('birth_date').value;

    if(password.length < 8) {
        alert('ตั้งรหัสมากกว่า 8 ตัวอักษรขึ้นไปจ้า!');
        window.location.reload(); 
    }
    
    else {
        
        axios.post("http://127.0.0.1:8000/sign_up", {
            "username": username,
            "password": password,
            "birth_date": birth_date,
            "role": role
        })
        .then((response) => {
        console.log(response.data);
        
        if(response.data == "Sign Up Successful") {
            window.location.href = 'sign_in.html';
            alert('ลงทะเบียนสำเร็จ!');
    
        } else if(response.data == "username is already taken") {
            alert('ชื่อนี้ถูกใช้แล้ว');
    
        } else {
            alert('เกิดข้อผิดพลาด กรุณาลองใหม่อีกครั้ง');
        }
    
        })
    }

    
    // console.log(response.data.response);
    // console.log(response.data.role);

    
}

