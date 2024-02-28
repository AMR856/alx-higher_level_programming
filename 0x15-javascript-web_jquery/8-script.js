const the_url = "https://swapi-api.alx-tools.com/api/films/?format=json";
$.get(the_url, function(respone)
{
    the_result = respone.results
    for(let i = 0; i < the_result.length; i++)
    {
        const listItem = $("<li>").text(the_result[i].title);
        $("UL#list_movies").append(listItem);
    }
});
