$(document).ready(function () {
  $('div#add_item').on('click', () => {
    $('ul.my_list').append('<LI>Item</LI>');
  });

  $('div#remove_item').on('click', () => {
    $('ul.my_list li:last-child').remove();
  });

  $('div#clear_list').on('click', () => {
    $('ul.my_list').empty();
  });
});
