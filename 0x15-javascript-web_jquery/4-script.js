function addClass (event) {
  $('header').toggleClass(function () {
    if ($(this).is('.red')) {
      $(this).removeClass('red');
      return 'green';
    } else {
      $(this).removeClass('green');
      return 'red';
    }
  });
}

$(document).ready(() => {
  $('div#toggle_header').click(addClass);
});
