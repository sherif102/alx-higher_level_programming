$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data, status)
{
    const movies = data.results;
    const list = $('#list_movies');
    $.each(movies, function(index, movie)
    {
        text = $('<li></li>').text(movie.title);
        list.append(text);
    });
});
