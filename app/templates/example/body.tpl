{% extends "base.tpl" %}

{% block body %}
  <div id="container">
    <nav class="navbar navbar-default" role="navigation">
      <div class="navbar-header">
        <a class="navbar-brand" href="{% url 'home' %}">DJBP</a>
      </div>
      <ul class="nav navbar-nav">
        <li><a href="{% url 'home' %}">Home</a></li>
        <li><a href="{% url 'foo' %}">Foo</a></li>
        <li><a href="{% url 'bar' %}">Bar</a></li>
      </ul>
    </nav>
    <div id="app-content">
      {% block content %}{% endblock %}
    </div>
  </div>
{% endblock %}