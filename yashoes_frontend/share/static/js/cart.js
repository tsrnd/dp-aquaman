$(document).ready(function () {
  $("#btn-add-cart").click(function () {
    $.ajax({
      type: 'POST',
      headers: {
        'Authorization': 'Bearer ' + readCookie('token'),
      },
      url: 'http://localhost:8000/api/cart/variant/',
      data: {
        CSRF: $('meta[name="csrf-token"]').attr('content'),
        'quantity': 1, //this will be replace by getting value when product detail data render implemented
        'variant_id': 1, //this will be replace by getting value when product detail data render implemented
      },
      success: function (data) {
        refreshCart()
      },
    });
  });
});