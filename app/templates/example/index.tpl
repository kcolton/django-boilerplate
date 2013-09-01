{% extends "example/body.tpl" %}

{% block content %}
<div class="wrap _meta-hasView" data-view="Home">
    <h1>Hello Boilerplate World!</h1>
    <p>
        <img src="{{ 'img/stick.jpg'|static }}">
    </p>
    <p>
        <a href="{% url 'foo' %}" class="btn btn-primary"><i class="icon icon-heart"></i> Sauce!</a>
    </p>
</div>
{% endblock %}