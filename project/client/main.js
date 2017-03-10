$(() => {
  console.log('sanity check!');
});

$('form').on('submit', (e) => {
  e.preventDefault();
  return add($('textarea').val())
  .then((res) => {
    $('#response').html('Success! <a href="http://localhost:5000/api/v1/stats/'+res.data.uuid+'">http://localhost:5000/api/v1/stats/'+res.data.uuid+'</a>');
  })
  .catch((err) => {
    $('#response').html('Error!');
  });
});

function add(data) {
  return $.ajax({
    method: 'POST',
    data: data,
    contentType: 'application/json',
    url: `http://localhost:5000/api/v1/stats`,
  });
}
