
const url = 'https://swapi.co/api/people/5/?format=json';

function addName (name) {
  $('DIV#character').text(name);
}

function successResponse (data) {
  addName(data.name);
}

function init () {
  $.ajax({
    url: url,
    method: 'GET'
  }).done(successResponse);
}

$(document).ready(init);
