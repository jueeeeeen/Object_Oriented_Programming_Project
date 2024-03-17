const create_chap_data = {};

    // book_name:str
    // chapter_number:int
    // name:str
    // context: str
    // cost : int

// create_chap_data.book_name = localStorage.getItem('');
localStorage.getItem("book_name_edit_last");

create_chap_data.book_name = localStorage.getItem("book_name_edit_last");
// create_chap_data.book_name = "Shin_chan";

function submit_create_chap() {
    create_chap_data.chapter_number = document.getElementById('chapter_number').value;
    create_chap_data.name = document.getElementById('chapter_name').value;
    create_chap_data.context = document.getElementById('context').value;
    create_chap_data.cost = document.getElementById('cost').value;

    const jsonDataString = JSON.stringify(create_chap_data);
    fetch(`/chapter`, {

        method: 'POST',
        headers: { 'Content-Type' : 'application/json' },

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

        if(data == "please try again") {
            const content = document.getElementById("content");
            content.innerHTML = `<p>Please Try Again</p>`;
        } else {

            const content = document.getElementById("content");
            content.innerHTML = `<p>Create Chapter Success</p>`;
        }
        
    })

    .catch((error) => {
        console.error("Error:", error);
    });
    success_form.style.display = 'block';
    setTimeout(function () {
        success_form.style.display = 'none';
        window.location.href = '../Templates/pre_edit_book.html';
    }, 3000);
}

function cancel_button() {
    window.location.reload(); 
}