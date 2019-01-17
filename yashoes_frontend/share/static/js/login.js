$(document).ready(function () {
  $("#btn-login").click(function () {
    $.ajax({
      url: 'http://localhost:8000/api/user/login/',
      type: "POST",
      data: {
        'username': $("#username").val(),
        'password': $("#password").val(),
        CSRF: $('meta[name="csrf-token"]').attr('content'),
      },
      contentType: "application/json; charset=utf-8", // this
      dataType: "html",
      success: function (data) {
        alert('cc')
      }
    });
  });

  // $("#logout").click(function () {
  //   $("form")[0].reset();
  //   $("#first").show();
  //   $("#second").hide();
  // });
});