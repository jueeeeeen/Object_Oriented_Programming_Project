async function pop_up_success_form() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    try {
        const response = await axios.post("http://127.0.0.1:8000/sign_up", { username, password });
        if (response.status === 200) {
            alert('เข้าสู่ระบบสำเร็จ!');
            window.location.href = 'homepage.html'; 
        } else {
            alert('เข้าสู่ระบบล้มเหลว! กรุณาตรวจสอบชื่อผู้ใช้และรหัสผ่านของคุณ');
        }
    } catch (error) {
        if (error.response.status === 422) {
            alert('ข้อมูลไม่ถูกต้อง กรุณาตรวจสอบอีกครั้ง');
        } else {
            alert('เกิดข้อผิดพลาดในการส่งคำขอ');
        }
        console.error(error);
    }
}
