let toc = document.querySelector('.md-content .toc');
if (toc) {
    let tocul = toc.querySelector('ul');
    let list = document.createElement('ol');

    for (let link of tocul.querySelectorAll('li a')) {
        let li = document.createElement('li');
        let a = document.createElement('a');
        li.appendChild(a);
        let id = link.getAttribute('href');
        console.log('fixing up %s', id);
        a.href = id;
        let head = document.querySelector(id);
        a.innerHTML = head.innerHTML;
        if (head.dataset.length) {
            li.append(` (${head.dataset.length})`);
        }
        list.appendChild(li);
    }

    tocul.replaceWith(list);
}
