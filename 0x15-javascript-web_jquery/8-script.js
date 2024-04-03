$.get('https://swapi-api.alx-tools.com/api/films/?format=json',
  (data) => {
    for (let i = 0; i < data.results.length; i++) {
      const item = $('<li></li>').text(data.results[i].title);
      $('ul#list_movies').append(item);
    }
  }
);
