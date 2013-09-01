{% extends "example/body.tpl" %}
{% from "macros/forms.tpl" import form_html %}

{% block content %}
  <h1>Form Example</h1>
  {{ form_html(form)|safe }}

  <br><br><br><br><br><br>

  <form method="POST">
    {{ form.as_p()|safe }}
  </form>

{% endblock %}