import katex from 'https://cdn.jsdelivr.net/npm/katex@0.12.0/dist/katex.mjs';
import renderMathInElement from 'https://cdn.jsdelivr.net/npm/katex@0.12.0/dist/contrib/auto-render.mjs';

let elts = document.querySelectorAll('.arithmatex');
console.log('have %d elements', elts.length);
for (let elt of elts) {
    renderMathInElement(elt);
}
