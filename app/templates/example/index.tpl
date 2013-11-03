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
  <h2>Manual Page Change</h2>
  <p>
    <button class="btn btn-default get-params">GET w/ Params</button>
    <button class="btn btn-default get-no-params">GET w/ No Params</button>
    <button class="btn btn-default post-data">POST w/ Data</button>
    <button class="btn btn-default post-no-data">POST w/ No Data</button>
  </p>
</div>
{% endblock %}