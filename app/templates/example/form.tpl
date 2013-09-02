{% extends "example/body.tpl" %}
{% import "macros/forms.tpl" as forms %}

{% block content %}
  <h1>Form Example</h1>
  {{ messages.html() }}
  {{ forms.form_html(form)|safe }}
{% endblock %}