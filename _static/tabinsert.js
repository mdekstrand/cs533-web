function setupTabStuff() {
  console.log('setting up slide tabs');
  $('.tabbed-set').each(function() {
    let elt = $('.tabbed-content.slides', this)[0];
    if (!elt) return;
    console.log('found slides', elt);
    let inp = $(elt).prev().prev();
    console.log('found input', inp);
    if (inp.tagName != 'input') {
      console.warn('unexpected element:', inp);
    }
    inp.on('change', function(evt) {
      if (inp[0].checked) {
        console.log('activating embed');
        $('.slide-container', elt).each(function() {
          console.log('container', this);
          if (!this.dataset.loaded) {
            let sid = this.dataset.id;
            let skey = this.dataset.key;
            $(this).append(`<iframe class=slide-embed src="https://onedrive.live.com/embed?resid=${sid}&amp;authkey=${skey}&amp;em=2&amp;wdAr=1.7777777777777777" frameborder="0">This is an embedded <a target="_blank" href="https://office.com">Microsoft Office</a> presentation, powered by <a target="_blank" href="https://office.com/webapps">Office</a>.</iframe>`)
            this.dataset.loaded = true;
          }
        });
      }
    });
  });
}

function adjustLinks() {
  console.log('adjusting links');
  $('a.external').attr('target', '_blank')
}

function adjustContent() {
  adjustLinks();
  setupTabStuff();
}

document.addEventListener('DOMContentLoaded', adjustContent);
