function getData()
{
    const code = $('#language_code').val();
    $.post('https://hellosalut.stefanbohacek.dev/', {"lang": code}, function(data)
    {
        $('#hello').text(data.hello);
    });
}
$('#btn_translate').on('click', getData);
$('#language_code').on('keypress', function(event){
    if (event.which === 13) {
        getData()
    }
});
