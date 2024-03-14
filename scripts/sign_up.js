
var sign_up_data = {}

document.getElementById('role').addEventListener('change', function() {
    sign_up_data.role = this.value;
});


function alert_success() {
    sign_up_data.username = document.getElementById('username').value;
    sign_up_data.password = document.getElementById('password').value;
    sign_up_data.birth_date = document.getElementById('birth_date').value;

    if((sign_up_data.username == "") || (sign_up_data.password == "") || (sign_up_data.birth_date == "") || (sign_up_data.role == "")) {
        alert('กรอกข้อมูลไม่ครบจ้าพี่');
    }

    if(sign_up_data.password.length < 8) {
        alert('ตั้งรหัสมากกว่า 8 ตัวอักษรขึ้นไปจ้า!');
        window.location.reload(); 
    }
    
    else {
        
        const jsonDataString = JSON.stringify(sign_up_data);
        fetch(`/sign_up`, {

            method: 'POST',
            headers: {'Content-Type' : 'application/json'},

            body: jsonDataString
        })
        .then((response) => {
            if (!response.ok) {
                throw new Error('Failed to submit comment');
            }
            return response.json();
        })
        .then(data => {
            console.log(data);
            // console.log(data.message);
    
            if(data == "Sign Up Successful") {
                window.location.href = 'sign_in.html';
                alert('ลงทะเบียนสำเร็จ!');
        
            } else if(data == "username is already taken") {
                alert('ชื่อนี้ถูกใช้แล้ว');
        
            } else {
                alert('เกิดข้อผิดพลาด กรุณาลองใหม่อีกครั้ง');
            }
    
        })
    }

    
    // console.log(response.data.response);
    // console.log(response.data.role);

    
}

