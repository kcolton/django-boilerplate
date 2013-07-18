{% extends "base.tpl" %}

{% block content %}
<h1>Hello Boilerplate World!</h1>
<p>
  <img src="{{ 'img/stick.jpg'|static }}">
</p>
<p>
    <a href="javascript:;" class="btn btn-primary"><i class="icon icon-heart"></i> Sauce</a>
</p>
{% endblock %}