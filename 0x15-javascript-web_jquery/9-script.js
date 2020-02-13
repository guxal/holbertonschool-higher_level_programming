
const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

function addText (hello) {
  $('DIV#hello').text(hello);
}

function successResponse (data) {
  addText(data.hello);
}

function init () {
  $.ajax({
    url: url,
    method: 'GET'
  }).done(successResponse);
}

$(document).ready(init);
