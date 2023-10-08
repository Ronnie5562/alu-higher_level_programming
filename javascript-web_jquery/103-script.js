$(document).ready(function () {
  $('#btn_translate, #language_code').on('click keyup', function (e) {
    if (e.type === 'click' || (e.type === 'keyup' && e.keyCode === 13)) {
      const languageCode = $('#language_code').val();

      $.getJSON('https://www.fourtonfish.com/hellosalut/hello/' + languageCode, function (data) {
        $('#hello').text(data.hello);
      });
    }
  });
});
