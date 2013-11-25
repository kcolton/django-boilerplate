{% extends "djbp/examples/body.tpl" %}

{% import "djbp/macros/messages.tpl" as msgs with context %}
{% import "djbp/macros/forms.tpl" as forms %}

{% block content %}
  <h1>Form Example</h1>
  {{ msgs.as_alerts() }}
  {{ forms.form(form)|safe }}
{% endblock %}