$('#add_item').on('click', function()
{
    item = $('<li></li>').text('Item');
    $('.my_list').append(item);
});
