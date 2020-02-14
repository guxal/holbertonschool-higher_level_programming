
const url = 'https://fourtonfish.com/hellosalut/?lang=:data';

function sendTranslate () {
  const lc = $('#language_code').val();

  $.ajax({
    url: url.replace(':data', lc),
    method: 'GET'
  }).done(successResponse);
}

function addText (hello) {
  $('DIV#hello').text(hello);
}

function successResponse (data) {
  addText(data.hello);
}

function init () {
  $('#btn_translate').click(sendTranslate);
}

$(document).ready(init);
