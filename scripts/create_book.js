const create_book_data = {};
    // name:str
    //  pseudonym:str
    //  writer_name:str
    //  genre: str
    //  prologue: str
    //  age_restricted: bool
    //  status: str 

// create_chap_data.book_name = localStorage.getItem('');
// localStorage.getItem("login_username");

// create_book_data.writer_name = localStorage.getItem("login_username");
create_book_data.writer_name = "Mozaza";

create_book_data.name = document.getElementById('book_name').value;
create_book_data.pseudonym = document.getElementById('pseudonym').value;
create_book_data.genre = document.getElementById('tag').value;
create_book_data.prologue = document.getElementById('prologue').value;
// create_book_data.age_restricted = document.getElementById('age_restricted').value;
// create_book_data.status = document.getElementById('status').value;


document.getElementById('status').addEventListener('change', function() {
    create_book_data.status = this.value;
});

document.getElementById('age_restricted').addEventListener('change', function() {
    create_book_data.age_restricted = this.value;
});

function submit_create_book() {
    create_book_data.name = document.getElementById('book_name').value;
    create_book_data.pseudonym = document.getElementById('pseudonym').value;
    create_book_data.genre = document.getElementById('tag').value;
    create_book_data.prologue = document.getElementById('prologue').value;
    // create_book_data.age_restricted = document.getElementById('age_restricted').value;

    const jsonDataString = JSON.stringify(create_book_data);
    fetch(`/book`, {

        method: 'POST',
        headers: { 'Content-Type' : 'application/json'},

        body: jsonDataString
        
    })
    .then((response) => {
        if (!response.ok) {
            throw new Error('Failed to submit comment');
        }
        return response.json();
        // console.log(response.data);

    // const content = document.getElementById("content");
    // content.innerHTML = `<p>${response.data}</p>`;
    })
    .then(data => {
        console.log(data);
        // console.log(data.message);

        const content = document.getElementById("content");
        content.innerHTML = `<p>Create Book Success</p>`;
        
    })



    .catch((error) => {
        console.error("Error:", error);
    });

    // window.location.href = '/page/writing';

    success_form.style.display = 'block';
    setTimeout(function () {
        success_form.style.display = 'none';
        window.location.href = '../Templates/my_writing.html';
      }, 3000);
}

function cancel_button() {
    window.location.reload(); 
}