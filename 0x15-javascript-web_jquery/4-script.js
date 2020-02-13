function addClass (event) {
  console.log('aqui');
  $('header').toggleClass(function () {
    console.log(this);

    if ($(this).is('.red')) {
      console.log('green');
      $(this).removeClass('red');
      return 'green';
    } else {
      console.log('not green');
      $(this).removeClass('green');
      return 'red';
    }
  });
}

$(document).ready(() => {
  $('div#toggle_header').click(addClass);
});
