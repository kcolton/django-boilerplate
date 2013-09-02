{%
  set tag_alert_map = {
    'debug': 'alert-info',
    'info': 'alert-info',
    'success': 'alert-success',
    'warning': 'alert-warning',
    'error': 'alert-danger'
  }
%}

{% macro as_alerts() %}
  {# Relies on messages being in the context #}
  {% for message in messages %}
    <div class="alert {{ tag_alert_map.get(message.tags, 'alert-info') }}">
      <a class="close" data-dismiss="alert">&times;</a>
      {{ message|safe }}
    </div>
  {% endfor %}
{% endmacro %}