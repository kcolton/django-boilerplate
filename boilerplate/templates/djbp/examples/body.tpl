{% extends "base.tpl" %}

{% block body %}
  <div class="container">
    <nav class="navbar navbar-default" id="app-navigation" role="navigation">
      <div class="navbar-header">
        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#app-navigation-collapse">
          <span class="sr-only">Toggle navigation</span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        <a class="navbar-brand" href="{% url 'home' %}">DJBP</a>
      </div>
      <div class="collapse navbar-collapse" id="app-navigation-collapse">
        <ul class="nav navbar-nav">
          <li><a href="{% url 'form_example' %}">Form</a></li>
          <li><a href="{% url 'messages_example' %}">Messages</a></li>
          <li class="dropdown">
            <a href="{% url 'links' %}" class="dropdown-toggle" data-toggle="dropdown">Link Types <b class="caret"></b></a>
            <ul class="dropdown-menu">
              <li><a href="{% url 'foo' %}">Relative URL</a></li>
              <li><a href="{{ '/bar/'|absolute_url(request) }}">Absolute Internal URL</a></li>
              <li><a href="http://github.com/kcolton/django-boilerplate">External URL</a></li>
              <li><a href="{% url 'redirect_internal' %}">Internal Redirect</a></li>
              <li><a href="{% url 'redirect_external' %}">External Redirect</a></li>
              <li><a href="{% url 'home' %}" data-hijax-ignore>No Hijax</a></li>
            </ul>
          </li>
          <li class="dropdown">
            <a href="#" class="dropdown-toggle" data-toggle="dropdown">Page Types <b class="caret"></b></a>
            <ul class="dropdown-menu">
              <li><a href="{% url 'json_example' %}" target="_blank">JSON</a></li>
              <li><a href="{% url 'csv_download_example' %}" target="_blank">CSV</a></li>
            </ul>
          </li>
          <li class="dropdown">
            <a href="#" class="dropdown-toggle" data-toggle="dropdown">Errors <b class="caret"></b></a>
            <ul class="dropdown-menu">
              <li><a href="{% url 'error_example' %}">500</a></li>
              <li><a href="/somethingthatdoesntexist/">404</a></li>
            </ul>
          </li>
          <li><a href="{% url 'bar' %}?cow=moo">Bar</a></li>
          <li><a href="{% url 'foo' %}?sauce=saucy">Foo</a></li>
          <li><a href="{% url 'log_example' %}">Log</a></li>
        </ul>
      </div>
    </nav>
    {% block content %}{% endblock %}
  </div>
{% endblock %}