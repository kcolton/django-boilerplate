{% extends "djbp/examples/body.tpl" %}

{% import "djbp/macros/messages.tpl" as msgs with context %}

{% block content %}
  <h1>Messages Example</h1>
  {{ msgs.as_alerts() }}
{% endblock %}