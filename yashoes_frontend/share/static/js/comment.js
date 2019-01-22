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
});