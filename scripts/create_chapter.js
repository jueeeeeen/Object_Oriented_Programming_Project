const create_chap_data = {};

    // book_name:str
    // chapter_number:int
    // name:str
    // context: str
    // cost : int

// create_chap_data.book_name = localStorage.getItem('');
localStorage.getItem("book_name_last");

create_chap_data.book_name = localStorage.getItem("book_name_last");


async function submit_create_chap() {
    create_chap_data.chapter_number = document.getElementById('chapter_number').value;
    create_chap_data.name = document.getElementById('chapter_name').value;
    create_chap_data.context = document.getElementById('context').value;
    create_chap_data.cost = document.getElementById('cost').value;

    axios.post("http://127.0.0.1:8000/chapter", {
        "book_name": create_chap_data.book_name,
        "chapter_number": create_chap_data.chapter_number,
        "name": create_chap_data.name,
        "context": create_chap_data.context,
        "cost": create_chap_data.cost
      })
      .then((response) => {
        console.log(response.data);

        // const content = document.getElementById("content");
        // content.innerHTML = `<p>${response.data}</p>`;
    })
    .catch((error) => {
        console.error("Error:", error);
    });

    // window.location.href = '/page/writing';

    // success_form.style.display = 'block';
    // setTimeout(function () {
    //     success_form.style.display = 'none';
    //     window.location.href = '/page/transaction.html';
    //   }, 3000);
}

function cancel_button() {
    window.location.reload(); 
}