const the_url = "https://swapi-api.alx-tools.com/api/people/5/?format=json";
$.get(the_url, function(data)
{
    $("DIV#character").text(data.name);
});
