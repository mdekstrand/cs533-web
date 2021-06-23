{% macro video(id) %}
    <div class="video-container video-embed">
    <iframe src="https://boisestate.hosted.panopto.com/Panopto/Pages/Embed.aspx?id={{id}}&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&start=0&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>
    </div>
{% endmacro %}
{% macro videojs(name) %}
    <div class="video-container">
    <video class="video-js vjs-theme-fantasy vjs-fluid" data-setup='{}' poster="{{extra.cdn}}/full/{{name}}_First_Frame.png" controls crossorigin='anonymous'>
    <source src="{{extra.cdn}}/full/{{name}}.mp4" type="video/mp4">
    <track kind="chapters" src="{{extra.cdn}}/full/{{name}}.toc.vtt" srclang="en">
    <track kind="captions" src="{{extra.cdn}}/full/{{name}}.vtt" srclang="en">
    <p>Your browser does not support HTML5 Video.</p>
    </video>
    </div>
{% endmacro %}
{% macro slides(resid, authkey) %}
    <div class=slide-container>
    <iframe class=slide-embed src="https://onedrive.live.com/embed?resid={{resid}}&amp;authkey={{authkey}}&amp;em=2&amp;wdAr=1.7777777777777777" frameborder="0">This is an embedded <a target="_blank" href="https://office.com">Microsoft Office</a> presentation, powered by <a target="_blank" href="https://office.com/webapps">Office</a>.</iframe>
    </div>
{% endmacro %}
{% macro vidtext(name) %}
<aside class="slides text hidden">
{% include 'videos/' + name + '.txt' %}
</aside>
{% endmacro %}
