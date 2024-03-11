
async function test() {
    event.preventDefault(); //ให้โชว์ content ค้างไว้

    const input = document.getElementById("username").value;
    const content = document.getElementById("content");
    console.log(input);

    const response = await axios.get(`http://127.0.0.1:8000/get_coin_transaction?username=${input}`);
    console.log(response.data);

    const coin_transaction = response.data.Coin_Transaction;

    if(coin_transaction && coin_transaction.length > 0) {
        for(let i = 0; i < coin_transaction.length; i++) {
            console.log(coin_transaction[i]);
            content.innerHTML += `<div><p> ${coin_transaction[i]} </p></div>`;

        }
    } else { 
        console.log("No coin transaction data available");
        content.innerHTML = "No coin transaction data available";
    }
    
}