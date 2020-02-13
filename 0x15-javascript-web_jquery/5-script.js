function addItem () {
  $('.my_list').append('<li>Item</li>');
}

function init () {
  $('div#add_item').click(addItem);
}

$(document).ready(init);
