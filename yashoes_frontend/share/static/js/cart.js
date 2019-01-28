//define global variable
var timeOut;

function addCart() {
  url = 'http://localhost:8000/api/user/cart/variant/';
  data = {
    'quantity': $('#slc-product-quantity').val(), //this will be replace by getting value when product detail data render implemented
    'variant_id': 4, //this will be replace by getting value when product detail data render implemented
  };
  token = readCookie('token');
  if (token != null) {
    data.CSRF = $('meta[name="csrf-token"]').attr('content');
    dataRequest = {
      token: readCookie('token'),
      data: data
    };
    sendRequest('POST', url, dataRequest, function (data) {
      refreshCart()
    })
  } else {
    data.product_name = $('#product-single-name').text();
    data.product_price = $('#product-single-price').text();
    data.product_color = $('#product-single-color').val();
    data.product_size = $('#product-single-size').val();
    data.product_image = $('#product-single-image').attr('src');
    setCartLocalStorage('cart', data)
  }
}

//cart handler
$(document).ready(function (c) {
  $('#form-user-info-transaction').validate({
    rules: {
      address: {
        required: true
      },
      phone_number: {
        required: true,
        minlength: 10,
        maxlength: 11
      }
    },
    messages: {
      address: {
        required: "Field is required"
      },
      phone_number: {
        required: "Field is required",
        minlength: "Phone number not valid",
        maxlength: "Phone number not valid"
      }
    }
  });

  $('.close').click(function () {
    parent = $(this).parent();
    token = readCookie('token');
    currentTab = parent.parent().children().length - 2;
    if (currentTab == 0) {
      $('#btn-cart-done').fadeOut('fast', function (c) {
        parent.remove();
      })
    }
    data = {
      CSRF: $('meta[name="csrf-token"]').attr('content'),
      variant_id: $(this).parent().attr('id'), //this will be replace by getting value when product detail data render implemented
    };
    if (token != null) {
      url = 'http://localhost:8000/api/user/cart/variant/';
      dataRequest = {
        token: token,
        data: data
      };
      sendRequest('DELETE', url, dataRequest, function (data) {
      })
    } else {
      cart = client.getItem('cart');
      cartData = JSON.parse(cart);
      index = cartData.findIndex(x => x.variant_id == data.variant_id);
      cartData.splice(index);
      if (cartData.length > 0) {
        client.setItem('cart', JSON.stringify(cartData))
      } else {
        client.removeItem('cart')
      }
    }
    parent.fadeOut('slow', function (c) {
      parent.remove();
    });
  });

  $('.btn-change-quantity').click(function (e) {
    data = {
      'variant_id': $(this).parent().parent().parent().attr('id'),
    };
    if ($(this).attr('id') == 'btn-minus') {
      decrementValue(e);
      data.quantity = -1
    } else {
      incrementValue(e);
      data.quantity = 1
    }
    clearTimeout(timeOut);
    token = readCookie('token');
    setCartLocalStorage('cart', data);
    if (token != null) {
      timeOut = setTimeout(function () {
        url = 'http://localhost:8000/user/sync/';
        dataRequest = {
          data: {
            'cart': client.getItem('cart'),
          }
        };
        sendRequest('POST', url, dataRequest, function (data) {
          localStorage.removeItem('cart');
        })
      }, 5000);
    }
  });

  $('#btn-cart-done').click(function () {
    let current = $(this);
    $(this).attr('disabled', 'disabled');
    if ($('#form-user-info-transaction').valid()) {
      let token = readCookie('token');
      if (token != null) {
        let url = 'http://localhost:8000/api/transaction/';
        let address = 'Da Nang';
        let phone_number = '0123456789';
        let dataRequest = {
          token: token,
          data: {
            'address': address,
            'phone_number': phone_number
          }
        };
        sendRequest('POST', url, dataRequest, function () {
          window.location.replace('http://localhost:8000/user/transactions/');
          current.removeAttr('disabled');
        }, function (data) {
          current.removeAttr('disabled');
          // console.log(data);
          let response = data.responseJSON;
          if (response != null && response.message != null) {
            alert(response.message)
          }
        })
      } else {
        alert('You are not login!');
      }
    } else {
      current.removeAttr('disabled')
    }
  })
});

//adding handle button decrease increase
function incrementValue(e) {
  e.preventDefault();
  var fieldName = $(e.target).data('field');
  var parent = $(e.target).closest('div');
  var currentVal = parseInt(parent.find('input[name=' + fieldName + ']').val(), 10);

  if (!isNaN(currentVal)) {
    parent.find('input[name=' + fieldName + ']').val(currentVal + 1);
  } else {
    parent.find('input[name=' + fieldName + ']').val(0);
  }
}

function decrementValue(e) {
  e.preventDefault();
  var fieldName = $(e.target).data('field');
  var parent = $(e.target).closest('div');
  var currentVal = parseInt(parent.find('input[name=' + fieldName + ']').val(), 10);

  if (!isNaN(currentVal) && currentVal > 0) {
    parent.find('input[name=' + fieldName + ']').val(currentVal - 1);
  } else {
    parent.find('input[name=' + fieldName + ']').val(0);
  }
}

//cart localstorage handler
function setCartLocalStorage(key, data) {
  client = localStorage;
  if (client.getItem(key) == null) {
    cartData = [];
    cartData.push(data);
    client.setItem(key, JSON.stringify(cartData))
  } else {
    cart = client.getItem(key);
    cartData = JSON.parse(cart);
    index = cartData.findIndex(x => x.variant_id == data.variant_id);
    if (index >= 0) {
      cartData[index].quantity = parseInt(cartData[index].quantity) + parseInt(data.quantity);
      client.setItem(key, JSON.stringify(cartData))
    } else {
      cartData.push(data);
      client.setItem(key, JSON.stringify(cartData))
    }
  }
}

function renderLocalCart() {
  var content = $();
  client = localStorage;
  cart = client.getItem('cart');
  cartData = JSON.parse(cart);
  itemCart = $("<ul id=\"test\" class=\"cart-header\">\n" +
    "              <div class=\"close\"></div>\n" +
    "              <li class=\"ring-in\"><a><img id='product-image' src='' alt='img' class=\"img-responsive\"\n" +
    "                                                             alt=\"\"></a>\n" +
    "              </li>\n" +
    "              <li><span id='product-name'>Elliot Shoes</span></li>\n" +
    "              <li><span id='product-price'>$ 300.00</span></li>\n" +
    "              <li>\n" +
    "                <div class=\"input-group\">\n" +
    "                  <input type=\"button\" value=\"-\" id='btn-minus' class=\"button-minus btn-change-quantity\" data-field=\"quantity\">\n" +
    "                  <input id='product-quantity' type=\"number\" step=\"1\" max=\"\" value=\"1\" name=\"quantity\" class=\"quantity-field\">\n" +
    "                  <input type=\"button\" value=\"+\" id='btn-plus' class=\"button-plus btn-change-quantity\" data-field=\"quantity\">\n" +
    "                </div>\n" +
    "              </li>\n" +
    "              <div class=\"clearfix\"></div>\n" +
    "            </ul>");
  $('#cart-content').html(function () {
    for (var i = 0; i < cartData.length; i++) {
      itemCart.attr('id', cartData[i].variant_id);
      itemCart.find('#product-name').text(cartData[i].product_name);
      itemCart.find('#product-image').attr('src', cartData[i].product_image);
      itemCart.find('#product-price').text(cartData[i].product_price);
      itemCart.find('#product-quantity').attr('value', cartData[i].quantity);
      content = content.add(itemCart).clone();
    }
    return content
  })
}

$(document).ready(function (c) {
  $(window).unload(function () {
    if (readCookie('token') != null) {
      localStorage.removeItem('cart');
    }
  });
});
