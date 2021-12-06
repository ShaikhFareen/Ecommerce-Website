var updateBtn = document.getElementsByClassName('updateCart');

function getToken(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
var csrftoken = getToken('csrftoken');



updating = function () {
  productId = this.dataset.product;
  action = this.dataset.action;
  console.log("Product-ID", productId, 'action', action, user)

  if (user == "AnonymousUser") {
    console.log("Not logged in")
  }
  else {
    updateUserOrder(productId, action)
  }
}

function updateUserOrder(productId, action) {
  var url = 'update_item';
  fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken
    },
    body: JSON.stringify({ 'productId': productId, 'action': action })
  })
  .then((response) => {
    return response.json()
  })
    .then((data) => {
      console.log('data:', data)
      location.reload()
    })

}

for (let i = 0; i < updateBtn.length; i++) {
  updateBtn[i].addEventListener('click', updating
  )

}
