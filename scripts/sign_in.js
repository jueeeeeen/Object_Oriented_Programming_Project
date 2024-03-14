function alert_success() {
    var username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    if(username == "" || password == "") {
        alert('กรอกข้อมูลไม่ครบจ้าพี่');
    }

    
    fetch(`/sign_in/?username=${username}&password=${password}`) // Make sure to pass parameters correctly
   
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to sign in'); // Modify the error message accordingly
        }
        return response.json();
    })
    .then(data => {
        console.log(data);

        if (data.response === "log in successfully") {
            window.location.href = 'homepage.html'; // Redirect to homepage upon successful login
            alert('Login successful!'); // Show a success message
            localStorage.setItem('login_username', username);
            localStorage.setItem('login_role', data.role);
        } else if (data.response === "wrong password") {
            alert('Login failed! Please check your username and password.'); // Show error message for wrong password
        } else {
            alert('An error occurred. Please try again.'); // Show a generic error message
        }
    })
    .catch(error => {
        console.error('Error:', error); // Log any errors
        alert('An error occurred. Please try again.');
    });
}
