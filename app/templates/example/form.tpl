{% extends "example/body.tpl" %}

{% import "macros/messages.tpl" as msgs with context %}
{% import "macros/forms.tpl" as forms %}

{% block content %}
  <h1>Form Example</h1>
  {{ msgs.as_alerts() }}
  {{ forms.form(form)|safe }}
{% endblock %}