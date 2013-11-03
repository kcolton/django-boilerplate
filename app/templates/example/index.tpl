{% extends "example/body.tpl" %}

{% import "macros/utils.tpl" as utils %}

{% block content %}
<div data-app-view="Home">
  <h1>Hello Boilerplate World!</h1>
  <p>
    <img src="{% static 'img/stick.jpg' %}">
  </p>
  <p>
    <a href="{% url 'foo' %}" class="btn btn-primary"><span class="glyphicon glyphicon-heart"></span> Sauce!</a>
  </p>
</div>
{% endblock %}