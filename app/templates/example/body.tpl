{% extends "base.tpl" %}

{% block body %}
<div id="top-bar">
  <div class="wrap">
    <a href="{% url 'home' %}">DJBP</a> |
    <a href="{% url 'home' %}">Home</a> |
    <a href="{% url 'foo' %}">Foo</a> |
    <a href="{% url 'bar' %}">Bar</a>
  </div>
</div>
<div id="app-content" class="wrap">
    {% block content %}{% endblock %}
</div>
{% endblock %}