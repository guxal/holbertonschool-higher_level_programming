
const url = 'https://fourtonfish.com/hellosalut/?lang=:data';

function sendTranslate () {
  const lc = $('#language_code').val();

  $.ajax({
    url: url.replace(':data', lc),
    method: 'GET'
  }).done(successResponse);
}

function keyEnter (event) {
  const keycode = (event.keyCode ? event.keyCode : event.which);

  if (keycode === 13) {
    sendTranslate();
  }
}

function addText (hello) {
  $('DIV#hello').text(hello);
}

function successResponse (data) {
  addText(data.hello);
}

function init () {
  $('#btn_translate').click(sendTranslate);

  $('#language_code').focus(() => {
    $(this).keypress(keyEnter);
  });
}

$(document).ready(init);
