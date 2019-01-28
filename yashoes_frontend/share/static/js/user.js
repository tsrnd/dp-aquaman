$(document).ready(function () {
  $('#profile-form').submit(function () {
    var emptyinputs = $(this).find('input').filter(function () {
      return !$.trim(this.value).length;
    }).prop('disabled', true);
  });
})