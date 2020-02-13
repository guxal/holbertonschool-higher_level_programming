function changeColor (event) {
  $('header').css('color', '#FF0000');
}

$(document).ready(() => {
  $('div#red_header').click(changeColor);
});
