var payment_data = {};

// localStorage
payment_data.username = localStorage.getItem("login_username");
// payment_data.username = "Mozaza";


document.getElementById('online_banking').addEventListener('click', function() {
    payment_data.payment_method = "OnlineBanking";
    console.log(payment_data.payment_method);
});

document.getElementById('debit_card').addEventListener('click', function() {
    payment_data.payment_method = "Debit Card";
    console.log(payment_data.payment_method);
});

document.getElementById('truemoney_wallet').addEventListener('click', function() {
    payment_data.payment_method = "TrueMoney Wallet";
    console.log(payment_data.payment_method);
});

const coin_boxes = document.querySelectorAll('.coin_box');

  coin_boxes.forEach(function(coin_box_click) {
      coin_box_click.addEventListener('click', function() {
          coin_boxes.forEach(function(box) {
            box.classList.remove('selected');
          });

          coin_box_click.classList.add('selected');
      });
  });

  const paymentButtons = document.querySelectorAll('.payment_button');

  paymentButtons.forEach(function(button) {
    button.addEventListener('click', function() {
      paymentButtons.forEach(function(btn) {
        btn.classList.remove('selected');
      });

      button.classList.add('selected');
    });
  });

document.getElementById('coin_box_click_20').addEventListener('click', function() {
    payment_data.golden_coin_amount = 20;
    console.log(payment_data.golden_coin_amount);
});

document.getElementById('coin_box_click_50').addEventListener('click', function() {
    payment_data.golden_coin_amount = 50;
    console.log(payment_data.golden_coin_amount);
});


document.getElementById('coin_box_click_100').addEventListener('click', function() {
    payment_data.golden_coin_amount = 100;
    console.log(payment_data.golden_coin_amount);
});

document.getElementById('coin_box_click_500').addEventListener('click', function() {
    payment_data.golden_coin_amount = 500;
    console.log(payment_data.golden_coin_amount);
});

document.getElementById('coin_box_click_costom').addEventListener('click', function() {
    payment_data.golden_coin_amount = document.getElementById('golden_coin_amount').value;
    console.log(payment_data.golden_coin_amount);
});

info_form = document.getElementById('info_form');
success_form = document.getElementById('success_form');

function pop_up_info_form() {
    payment_data.code = document.getElementById('promotion_code').value;
    payment_data.payment_info = document.getElementById('payment_info').value;
    console.log(payment_data);

    info_form.style.display = 'block';
}

function pop_up_success_form() {
    payment_data.code = document.getElementById('promotion_code').value;
    payment_data.payment_info = document.getElementById('payment_info').value;
    console.log(payment_data)

    const jsonDataString = JSON.stringify(payment_data)
    fetch(`/buy_coin`, {

        method: 'POST',
        headers: { 'Content-Type' : 'application/json'},

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

        const content = document.getElementById("content");
        content.innerHTML = `<p>${data}</p>`;
        
    })

    .catch((error) => {
        console.error("Error:", error);
    });

    success_form.style.display = 'block';
    setTimeout(function () {
        success_form.style.display = 'none';
        window.location.href = '../Templates/transaction.html';
    }, 3000);
}


function cancel_button() {
    window.location.reload(); 
}

function pop_all_down() {
    console.log("yayyy");
}