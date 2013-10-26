{% macro html_attrs(d) %}
  {%- for attr,val in d.iteritems() -%}
    {{ ' ' if not loop.first }}{{ attr }}{% if val %}="{{ val }}"{% endif %}
  {%- endfor -%}
{% endmacro %}

{% macro alert(message, level='info', closable=True, extra_classes=None) -%}
  <div class="alert alert-{{ level }} {{ extra_classes if extra_classes }}">
    {% if closable %}<a class="close" data-dismiss="alert">&times;</a>{% endif %}
    {{ message|safe }}
  </div>
{%- endmacro %}

