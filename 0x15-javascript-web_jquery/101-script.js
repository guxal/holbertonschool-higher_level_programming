function addItem () {
  $('UL.my_list').append('<li>Item</li>');
}

function removeItem () {
  if ($('UL.my_list').find('li').length) {
    $('UL.my_list').find('li')[0].remove();
  }
}

function clearList () {
  $('UL.my_list').empty();
}

function init () {
  $('DIV#add_item').click(addItem);
  $('DIV#remove_item').click(removeItem);
  $('DIV#clear_list').click(clearList);
}

$(document).ready(init);
