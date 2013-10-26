{% extends "base.tpl" %}

{% block body %}
  <div id="container">
    <nav class="navbar navbar-default" role="navigation">
      <div class="navbar-header">
        <a class="navbar-brand" href="{% url 'home' %}">DJBP</a>
      </div>
      <ul class="nav navbar-nav">
        <li><a href="{% url 'home' %}">Home</a></li>
        <li><a href="{% url 'form_example' %}">Form Example</a></li>
        <li><a href="{% url 'messages_example' %}">Messages Example</a></li>
        <li><a href="{% url 'redirect_internal' %}">Redirect Internal</a></li>
        <li><a href="{% url 'home' %}" data-app-no-hijax>No Hijax</a></li>
        <li><a href="{% url 'foo' %}">Foo</a></li>
        <li><a href="{% url 'bar' %}">Bar</a></li>
        <li><a href="{% url 'json_example' %}" target="_blank">JSON</a></li>
        <li><a href="{% url 'csv_download_example' %}" target="_blank">CSV Download</a></li>
      </ul>
    </nav>
    <div id="app-content">
      {% block content %}{% endblock %}
    </div>
  </div>
{% endblock %}