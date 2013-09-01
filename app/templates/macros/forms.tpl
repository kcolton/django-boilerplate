{% macro form_field_html(field) %}
  {{ field|safe }}
{% endmacro %}


{% macro form_field_text_html(field) %}
  {{ field|add_class("form-control")|safe }}
{% endmacro %}


{%
   set field_map = {
    'TextInput': form_field_text_html,
    'DateInput': form_field_text_html,
    'DateTimeInput': form_field_text_html
   }
%}


{% macro form_row_html(field) %}
  <div class="form-group{{ ' has-error' if field.errors }}">
    <div>{{ field.field.widget.__class__.__name__ }}</div>

    {{ field.label_tag()|safe }}

    {# Look at the type of field widget to see how to render it #}
    {% if field_map[field.field.widget.__class__.__name__] %}
      {{ field_map[field.field.widget.__class__.__name__](field) }}
    {% else %}
      {{ form_field_html(field) }}
    {% endif %}

    {% for error in field.errors %}
      <p class="help-block">{{ error }}</p>
    {% endfor %}

    {% if field.help_text %}
      <p class="help-block">{{ field.help_text|safe }}</p>
    {% endif %}
  </div>
{% endmacro %}


{% macro form_body_html(form) %}

  {{ form.non_field_errors()|safe }}

  {# visible and hidden fields #}

  {% for field in form %}
    {{ form_row_html(field) }}
  {% endfor %}

{% endmacro %}


{% macro form_html(form) %}
  <form method="POST" role="form"{{ ' enctype="multipart/form-data' if form.is_multipart }}>
    {{ form_body_html(form) }}
    <button type="submit" class="btn btn-primary">Submit</button>
  </form>
{% endmacro %}