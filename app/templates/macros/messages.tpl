{% macro as_alerts() %}
  {# Relies on messages being in the context #}
  {% for message in messages %}
    <div class="alert{% if message.tags %} alert-{{ message.tags }}{% endif %}">
      <a class="close" data-dismiss="alert">&times;</a>
      {{ message }}
    </div>
  {% endfor %}
{% endmacro %}