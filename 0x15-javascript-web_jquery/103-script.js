$(document).ready(function () {
  function translate () {
    $('DIV#hello').empty();
    const l = $('INPUT#language_code').val();
    $.ajax({
      type: 'GET',
      url: 'https://fourtonfish.com/hellosalut/?lang=' + l,
      success: function (data) {
        $('DIV#hello').append(data.hello);
      }
    });
  }
  $('INPUT#btn_translate').click(function () {
    translate();
  });
  $('INPUT#language_code').keypress(function (e) {
    const k = e.which;
    if (k === 13) {
      translate();
    }
  });
});
