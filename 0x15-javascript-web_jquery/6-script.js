function updateHeader () {
  $('header').text('New Header!!!');
}

function init () {
  $('div#update_header').click(updateHeader);
}

$(document).ready(init);
