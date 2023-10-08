// displays the value of hello from a fetch in the HTML tag DIV#hello
$(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data, textStatus) {
    $('#hello').text(data.hello);
  });
});
