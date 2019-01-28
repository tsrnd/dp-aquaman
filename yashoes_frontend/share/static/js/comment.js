$(document).ready(function () {
  $(document).on("click", "#btn-reply", function () {
    $(this).parent().parent().parent().parent().find('.comment-box').css('display', 'block')
  });

  $(document).on("click", "#btn-reply-cancel", function () {
    $(this).parent().parent().css('display', 'none')
  });


  $("#rateYo").rateYo({
    rating: $("#rateYo").attr('value'),
    fullStar: true,
    onSet: function (e, data) {
      vote(data.rating())
    },
    starWidth: "40px"
  });

  function vote(rating) {
    var url = window.location.pathname;
    var id = url.substring(url.lastIndexOf('/') + 1);
    if (confirm("Do you want vote " + rating + " star for this product?")) {
      $.ajax({
        url: 'http://localhost:8000/api/products/' + id + '/rating',
        headers: {
          'Authorization': 'Bearer ' + readCookie('token'),
        },
        type: 'POST',
        data: {
          CSRF: $('meta[name="csrf-token"]').attr('content'),
          rating: rating
        }, statusCode: {
          200: function (response) {
            alert("success")
            $("#rateYo").rateYo("option", "readOnly", true);
            $("#rateYo").rateYo("option", "rating", response.average_rating)
          },
          400: function (response) {
            alert(response.responseJSON.message_error)
          },
          405: function (response) {
            alert('You can vote only one time')
          }
        }
      })
    }
  }

  $('.btn-comment').click(function (){
    var url = window.location.pathname;
    var id = url.substring(url.lastIndexOf('/') + 1);
    parent = $(this).parent()
    commentBoxClass = $(this).parent().parent()
    postComment('http://localhost:8000/api/products/'+id+'/comments', parent, commentBoxClass)
  });

  $('.btn-delete-comment').click(function(){
    if (confirm("Do you want delete this comment?")) {
      parent = $(this).parent()
      var id = parent.attr('id')
      $.ajax({
        url: 'http://localhost:8000/api/comments/'+id,
        headers: {
          'Authorization': 'Bearer ' + readCookie('token'),
        },
        type:'DELETE',
        data: {
          CSRF: $('meta[name="csrf-token"]').attr('content'),
        },
        success: function(data) {
          console.log(200)
        },
        statusCode: {
          200: function(response){
            $("#"+id).remove()
          }
        }
      })
    }
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
      400: function (response) {
        alert('400', response)
      },
      401: function (response) {
        alert(401)
      },
      404: function (response) {
        alert(404)
      }
    }
  })
}