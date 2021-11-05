let input = document.getElementById('input');
let output = document.getElementById('output');

function handleNewText(evt) {
  let str = evt.target.value;
  str = str.trim();
  if (str.startsWith('<iframe')) {
    let box = document.getElementById('container')
    box.innerHTML = str;
    let iframe = box.firstElementChild;
    let url = iframe.getAttribute('src');
    url = new URL(url);
    console.log('extracted url', url);
    let rid = url.searchParams.get('resid');
    let auth = url.searchParams.get('authkey');
    let txt = `${rid}\t${auth}`;
    output.value = txt;
    navigator.clipboard.writeText(txt);
  }
}

input.onchange = handleNewText;
console.log('ready to go');
