$(document).ready(function () {
  $("#login-form").submit(function (eventObj) {
    console.log('ahihi');
    client = localStorage;
    cart = client.getItem('cart');
    var input = $("<input>")
        .attr("type", "hidden")
        .attr("name", "cart").val(cart);
    $('#login-form').append(input);
    client.removeItem('cart');
  });
});
