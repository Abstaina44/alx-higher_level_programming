$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const lang = $('#language_code').val();
    $.ajax({
      url: `https://hellosalut.stefanbohacek.dev/?lang=${lang}`,
      type: 'GET',
      dataType: 'json'
    }).done(function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
