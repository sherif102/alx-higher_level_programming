const element = $('.my_list');
$('#add_item').on('click', function()
{
    const list = $('<li></li>').text('Item');
    element.append(list);
});

$('#remove_item').on('click', function()
{
    const lastList = $('ul.my_list li:last-child')
    lastList.detach();
});

$('#clear_list').on('click', function()
{
    element.empty();
});
