function displayChapterEditAndNavigate(chapter_id) {
    localStorage.setItem('chapter_id_last', chapter_id)
    window.location.href = "edit_chap_temp.html";
}

document.addEventListener('DOMContentLoaded', async function () {
    const editChapterForm = document.getElementById('editChapterForm');
    const chapterIdInput = document.getElementById('chapter_id');
    const chapterNumberInput = document.getElementById('chapter_number');
    const nameInput = document.getElementById('name');
    const contextInput = document.getElementById('context');
    const costInput = document.getElementById('cost');

    try {
        // Retrieve existing chapter information from the server
        // const chapterId = 'Shin_chan-1'
        const chapterId = localStorage.getItem('chapter_id_last'); 
        console.log(chapterId);
        const response = await fetch(`/chapter/info/${chapterId}`);
        if (!response.ok) {
            throw new Error('Failed to fetch chapter information');
        }
        const chapterData = await response.json();
        console.log("before chapterData: ", chapterData)
        // Populate form fields with existing chapter information
        chapterIdInput.value = chapterData.chapter_id;
        nameInput.value = chapterData.name;
        chapterNumberInput.value = chapterData.chapter_number
        contextInput.value = chapterData.context;
        costInput.value = chapterData.price;
    } catch (error) {
        console.error('Error fetching chapter information:', error);
    }

    if (editChapterForm) {
        editChapterForm.addEventListener('submit', async function (event) {
            event.preventDefault();

            try {
                const formData = new FormData(this);
                const jsonData = {};
                formData.forEach((value, key) => {
                    jsonData[key] = value;
                });
                console.log(jsonData);
                console.log("start post method");
                const response = await fetch('/edit_chapter', {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(jsonData)
                });

                if (!response.ok) {
                    throw new Error('Failed to edit chapter');
                }
                const data = await response.json();
                console.log("data after", data);
                if (response) {
                    console.log("data.value:", data.message)
                    response.innerText = data.message;
                }
                go_to_pre_edit_book();
            } catch (error) {
                console.error('Error editing chapter:', error);
            }
        });
    }
});
function go_to_pre_edit_book() {
    const book_name = localStorage.getItem("book_name_last")
    // const chapterId = "Shin_chan-1"
    displayPreEditBookAndNavigate(book_name)
}

function go_to_chapter_info() {
    // const chapterId = localStorage.getItem("chapter_name_last")
    const chapterId = "Shin_chan-1"
    NavigateToChapterInfo(chapterId)
}