// Code based in: https://codepen.io/srph/pen/rxoLMG?editors=0010

var number_of_tags = 5
var tags = [];
var $container = document.querySelector('.tag-field');
var $input = document.querySelector('.js-tag-input');
var $tags = document.querySelector('.js-tags');

$container.addEventListener('click', function() {
  $input.focus();
});

$container.addEventListener('keydown', function(evt) {
  if ( !evt.target.matches('.js-tag-input') ) {
    return;
  }
  
  if ( evt.keyCode !== 13 ) {
    return;
  }
  
  var value = String(evt.target.value);
  
  if ( !value.length || value.length > 20 || tags.length === number_of_tags ) {
    return;
  }
  
  tags.push(evt.target.value);
  $input.value = '';
  render(tags, $tags);
});

$container.addEventListener('keydown', function(evt) {
  if ( !evt.target.matches('.js-tag-input') ) {
    return;
  }
  
  if ( evt.keyCode !== 8 ) {
    return;
  }
  
  if ( String(evt.target.value).length ) {
    return;
  }
  
  tags = tags.slice(0, tags.length - 1);
  $input.value = '';
  render(tags, $tags);
});

$container.addEventListener('click', function(evt) {
  if ( evt.target.matches('.js-tag-close') || evt.target.matches('.js-tag') ) {
    tags = tags.filter(function(tag, i) {
      return i != evt.target.getAttribute('data-index');
    });
    render(tags, $tags);
  }
}, true);
 

function render(tags, el) {
console.log(tags)
  el.innerHTML = tags.map(function(tag, i) {
    return (
      '<div class="tag js-tag" data-index="' + i + '">' +
        tag +
        '<span class="tag-close js-tag-close" data-index="' + i + '">×</span>' +
      '</div>'
   );
  }).join('') + (tags.length === number_of_tags ? '' : '<input placeholder="Adicione tags..." class="js-tag-input">')
  ;
  
  $container.querySelector('.js-tag-input').focus();
}