function addClass (event) {
  $('header').addClass('red');
}

$(document).ready(() => {
  $('div#red_header').click(addClass);
});
