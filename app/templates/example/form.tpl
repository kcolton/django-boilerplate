{% extends "example/body.tpl" %}
{% import "macros/messages.tpl" as msgs with context %}
{% import "macros/forms.tpl" as forms %}

{% block content %}
  <div class="_meta-view" data-view="FormExample">
    <h1>Form Example</h1>
    {{ msgs.as_alerts() }}
    {{ forms.form_html(form, extra_classes="hijax")|safe }}
  </div>
{% endblock %}