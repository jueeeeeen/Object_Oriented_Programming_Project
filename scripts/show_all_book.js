//show_all_book
show_all_book();
function show_all_book(){
    fetch('/search_all', {
        method: 'GET',
    })
    .then(resp => resp.json())
    .then(data => {
        console.log(data);
        // const search_input = document.getElementById("searchInputPage")
        // search_input.value = search_str;
        // current_data = data;
        // $('#search_result_page').empty();
        // show_type(data);
    })
    .catch(error => {
        console.error(error);
    });
}