function readCookie(name) {
  var nameEQ = name + "=";
  var ca = document.cookie.split(';');
  for (var i = 0; i < ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') c = c.substring(1, c.length);
    if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
  }
  return null;
}

function refreshCart() {
  $.ajax({
    type: 'GET',
    headers: {
      'Authorization': 'Bearer ' + readCookie('token'),
    },
    url: 'http://localhost:8000/api/user/cart/information/',
    success: function (response) {
      $('#cart-quantity').text(response.total)
    },
  });
}

function sendRequest(method, url, dataRequest, onSuccess, onFailed = {}) {
  let headers = {
    'X-CSRFToken': $('meta[name="csrf-token"]').attr('content'),
  };
  if (dataRequest.token != null) {
    headers.Authorization = 'Bearer ' + dataRequest.token;
  }
  $.ajax({
    type: method,
    url: url,
    data: dataRequest.data,
    headers: headers,
    success: onSuccess,
    error: onFailed
  });
}
