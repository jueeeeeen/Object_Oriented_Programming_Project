document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('addChapterButton').addEventListener('click', function() {
        window.location.href = "create_chapter.html"; 
    });

    function displayPreEditBookAndNavigate(bookName) {
        console.log("start");

        fetch(`/book/${bookName}`)
            .then(response => response.json())
            .then(data => {
                console.log("oooo")
                sessionStorage.setItem('PreEditBook', JSON.stringify(data));

                const PreEditBook = JSON.parse(sessionStorage.getItem('PreEditBook'));

                console.log("Retrieved book information:", data);

                if (PreEditBook && PreEditBook.genre && PreEditBook.name && PreEditBook.pseudonym && PreEditBook.prologue && PreEditBook.writer_name && PreEditBook.date_time) {

                    document.getElementById('genre').textContent = PreEditBook.genre;
                    document.getElementById('bookName').textContent = PreEditBook.name;
                    document.getElementById('prologueInfo').textContent = PreEditBook.prologue;
                    document.getElementById('prologueDisplay').textContent = PreEditBook.prologue;
                    document.getElementById('pseudonymInfo').textContent = PreEditBook.pseudonym;
                    document.getElementById('pseudonymDisplay').textContent = PreEditBook.pseudonym;
                    document.getElementById('writer_username').textContent = PreEditBook.writer_name;
                    document.getElementById('date_time').textContent = PreEditBook.date_time;
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }
});
