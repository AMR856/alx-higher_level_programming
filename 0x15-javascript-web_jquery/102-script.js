$(function()
{
    const the_url = "https://www.fourtonfish.com/hellosalut/";
    the_lang = $("INPUT#language_code").val();
    the_full_url = the_url + '?&lang=' + toString(the_lang);
    $("INPUT#btn_translate").click( function() {
        $.get(the_full_url, function(respone)
        {
            the_result = respone.hello
            $("DIV#hello").html(the_result);
        });
    });
});
