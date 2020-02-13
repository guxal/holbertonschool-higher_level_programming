
const url = 'https://swapi.co/api/films/?format=json';

function addItem (title) {
  $('UL#list_movies').append(`<li>${title}</li>`);
}

function successResponse (data) {
  data.results.forEach((v, i) => {
    addItem(v.title);
  });
}

function init () {
  $.ajax({
    url: url,
    method: 'GET'
  }).done(successResponse);
}

$(document).ready(init);
