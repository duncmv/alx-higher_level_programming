$.get('https://hellosalut.stefanbohacek.dev/?lang=fr',
  (data) => {
    $('div#hello').text(data.hello);
  }
);
