$(function()
{
    const the_url = "https://hellosalut.stefanbohacek.dev/?lang=fr";
    $.get(the_url, function(respone)
    {
        $("DIV#hello").text(respone.hello)
    });
});
