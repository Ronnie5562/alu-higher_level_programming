// fetches a character name with an API
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
  $('#character').text(data.name);
});
