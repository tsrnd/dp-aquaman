//define global variable
var timeOut;
var points = 0;


function addCart() {
  url = 'http://localhost:8000/api/user/cart/variant/';
  data = {
    'quantity': $('#slc-product-quantity').val(), //this will be replace by getting value when product detail data render implemented
    'variant_id': 1, //this will be replace by getting value when product detail data render implemented
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
    setCartLocalStorage('cart', data)
  }
}

$(document).ready(function (c) {
  $('.close').click(function () {
    parent = $(this).parent();
    currentTab = parent.parent().children().length - 2;
    if (currentTab == 0) {
      $('#btn-cart-done').fadeOut('fast', function (c) {
        parent.remove();
      })
    }
    url = 'http://localhost:8000/api/user/cart/variant/';
    dataRequest = {
      token: readCookie('token'),
      data: {
        CSRF: $('meta[name="csrf-token"]').attr('content'),
        variant_id: 1, //this will be replace by getting value when product detail data render implemented
      }
    };
    sendRequest('DELETE', url, dataRequest, function (data) {
      parent.fadeOut('slow', function (c) {
        parent.remove();
      });
    })
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

$(document).ready(function (c) {
  $('.input-group').on('click', '.button-plus', function (e) {
    points++;
    incrementValue(e);
    clearTimeout(timeOut);
    timeOut = setTimeout(function () {
      url = 'http://localhost:8000/api/user/cart/variant/';
      data = {
        CSRF: $('meta[name="csrf-token"]').attr('content'),
        'quantity': points, //this will be replace by getting value when product detail data render implemented
        'variant_id': 1, //this will be replace by getting value when product detail data render implemented
      };
      dataRequest = {
        token: readCookie('token'),
        data: data
      };
      sendRequest('POST', url, dataRequest, function (data) {
        points = 0
      })
    }, 5000);
  });

  $('.input-group').on('click', '.button-minus', function (e) {
    points--;
    decrementValue(e);
    clearTimeout(timeOut);
    timeOut = setTimeout(function () {
      url = 'http://localhost:8000/api/user/cart/variant/';
      data = {
        CSRF: $('meta[name="csrf-token"]').attr('content'),
        'quantity': points, //this will be replace by getting value when product detail data render implemented
        'variant_id': 1, //this will be replace by getting value when product detail data render implemented
      };
      dataRequest = {
        token: readCookie('token'),
        data: data
      };
      sendRequest('POST', url, dataRequest, function (data) {
        points = 0
      })
    }, 5000);
  });
});

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
    console.log(cartData);
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
      "              <li class=\"ring-in\"><a href=\"single.html\"><img id='product-image' src='' class=\"img-responsive\"\n" +
      "                                                             alt=\"\"></a>\n" +
      "              </li>\n" +
      "              <li><span id='product-name'>Elliot Shoes</span></li>\n" +
      "              <li><span id='product-price'>$ 300.00</span></li>\n" +
      "              <li>\n" +
      "                <div class=\"input-group\">\n" +
      "                  <input type=\"button\" value=\"-\" class=\"button-minus\" data-field=\"quantity\">\n" +
      "                  <input id='product-quantity' type=\"number\" step=\"1\" max=\"\" value=\"1\" name=\"quantity\" class=\"quantity-field\">\n" +
      "                  <input type=\"button\" value=\"+\" class=\"button-plus\" data-field=\"quantity\">\n" +
      "                </div>\n" +
      "              </li>\n" +
      "              <div class=\"clearfix\"></div>\n" +
      "            </ul>");
  $('#cart-content').html(function () {
    for (var i = 0; i < cartData.length; i++) {
      itemCart.find('#product-name').text(cartData[i].product_name);
      itemCart.find('#product-image').attr('src', cartData[i].product_image);
      itemCart.find('#product-price').text(cartData[i].product_price);
      itemCart.find('#product-quantity').attr('value', cartData[i].quantity);
      content = content.add(itemCart).clone();
    }
    return content
  })
}
