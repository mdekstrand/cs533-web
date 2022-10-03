function setupTabStuff() {
  console.log('setting up slide tabs');
  $('.sd-tab-set').each(function() {
    let elt = $('.sd-tab-content.slides', this)[0];
    if (!elt) return;
    console.log('found slides', elt);
    let inp = $(elt).prev().prev();
    console.log('found input', inp);
    inp.on('change', function(evt) {
      if (inp[0].checked) {
        console.log('activating embed');
        $('.slide-container', elt).each(function() {
          console.log('container', this);
          if (!this.dataset.loaded) {
            // let sid = this.dataset.id;
            // let skey = this.dataset.key;
            let embed = new URL('https://view.officeapps.live.com/op/embed.aspx');
            let base = window.location;
            let slideURL = new URL(dataset.file, base);
            embed.searchParams.append('src', slideURL.toString());
            $(this).append(`<iframe class=slide-embed src="${embed}" frameborder="0">This is an embedded <a target="_blank" href="https://office.com">Microsoft Office</a> presentation, powered by <a target="_blank" href="https://office.com/webapps">Office</a>.</iframe>`)
            this.dataset.loaded = true;
          }
        });
      }
    });
  });
}

function adjustLinks() {
  console.log('adjusting links');
  $('a.external').attr('rel', 'noopener')
  $('a.external').attr('target', '_blank')
}

function adjustContent() {
  adjustLinks();
  setupTabStuff();
}

document.addEventListener('DOMContentLoaded', adjustContent);
