$('#btn_translate').on('click', function()
{
    const code = $('#language_code').val();
    $.post('https://hellosalut.stefanbohacek.dev/', {"lang": code}, function(data)
    {
        $('#hello').text(data.hello);
    });
});
