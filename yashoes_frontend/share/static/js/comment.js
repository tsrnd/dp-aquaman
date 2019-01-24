$(document).ready(function () {
  $(document).on("click", "#btn-reply", function () {
    $(this).parent().parent().parent().parent().find('.comment-box').css('display', 'block')
  });

  $(document).on("click", "#btn-reply-cancel", function () {
    $(this).parent().parent().css('display', 'none')
  });

  $("#rateYo").rateYo({
    rating: 3.7
  });

  $(document).on("click", "#btn-comment", function () {
    parent = $(this).parent()
    commentBoxClass = $(this).parent().parent()
    postComment('http://localhost:8000/api/products/1/comments', parent, commentBoxClass)
  });
});

function postComment(url, parent, commentBox) {
  var content = parent.find('#content-comment').val()
  $.ajax({
    url: url,
    headers: {
      'Authorization': 'Bearer ' + readCookie('token'),
    },
    type: 'POST',
    data: {
      CSRF: $('meta[name="csrf-token"]').attr('content'),
      content: content,
      parent_comment_id: parent.attr('id')
    },
    success: function (data) {
      console.log(200)
    },
    statusCode: {
      200: function (response) {
        location.reload()
      },
      401: function (response) {
        alert(401)
      },
      404: function (response) {
        alert(404)
      },
      400: function (response) {
        alert('400', response)
      },
    }
  })
}