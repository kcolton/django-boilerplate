{% extends "example/body.tpl" %}

{% macro logger_info(logger) %}
<ul>
  <li>Class: {{ logger|classname }}</li>
  <li>Disabled: {{ logger.disabled }}</li>
  <li>Filters: {{ logger.filters|pprint }}</li>
  <li>Handlers: {{ logger.handlers|pprint }}</li>
  <li>Level: {{ logger.level }}</li>
  <li>Name: {{ logger.name }}</li>
  <li>Parent: {{ logger.parent }}</li>
  <li>Propagate: {{ logger.propagate }}</li>
</ul>
{% endmacro %}

{% block content %}
  <h1>Log Test!</h1>
  <p>Check your logs!</p>
  <h2>Loggers</h2>

  <ul>
    <li>
      <h3>root</h3>
      {{ logger_info(manager.root) }}
    </li>
    {% for namespace, logger in manager.loggerDict|dictsort %}
    <li>
      <h3>{{ namespace }}</h3>
      {{ logger_info(logger) }}
    </li>
    {% endfor %}
  </ul>

{% endblock %}