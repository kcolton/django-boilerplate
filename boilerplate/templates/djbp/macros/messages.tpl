{% import "djbp/macros/utils.tpl" as utils %}

{%
  set tag_alert_map = {
    'debug': 'info',
    'info': 'info',
    'success': 'success',
    'warning': 'warning',
    'error': 'danger'
  }
%}

{% macro as_alerts() -%}
  {% for message in messages %}
    {{ utils.alert(message, tag_alert_map.get(message.tags, 'info'), closable=True) }}
  {% endfor %}
{%- endmacro %}