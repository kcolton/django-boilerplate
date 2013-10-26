{# Inspired by: https://github.com/tzangms/django-bootstrap-form/ #}

{% import "macros/utils.tpl" as utils %}

{% macro form_row_html(field) %}
  <div class="form-group{{ ' has-error' if field.errors }}" data-field-type="{{ field.field.widget.__class__.__name__ }}">

    {# Look at the type of field widget to see how to render it #}
    {% if field|is_checkbox %}
      <div class="checkbox">
        <label>{{ field|safe }} {{ field.label }}</label>
      </div>
    {% elif field|is_radio %}
      {{ field.label_tag()|safe }}
      {% for choice in field %}
        <div class="radio">
          <label>{{ choice.tag()|safe }} {{ choice.choice_label }}</label>
        </div>
      {% endfor %}
    {% elif field|is_checkbox_multiple %}
      {# Where is the bootstrapy HTML? Nowhere until django 1.6 lands and un-retards CheckboxSelectMultiple #}
      {{ field.label_tag()|safe }}
      {{ field|safe }}
    {% else %}
      {{ field.label_tag()|safe }}
      {{ field|add_class("form-control")|safe }}
    {% endif %}

    {% for error in field.errors %}
      <span class="help-block">{{ error }}</span>
    {% endfor %}

    {% if field.help_text %}
      <p class="help-block">{{ field.help_text|safe }}</p>
    {% endif %}
  </div>
{% endmacro %}


{% macro form_body_html(form) %}

  {% if form.non_field_errors() %}
    <div class="alert alert-danger">
      <a class="close" data-dismiss="alert">&times;</a>
      {% for non_field_error in form.non_field_errors() %}
        {{ non_field_error }}
      {% endfor %}
    </div>
  {% endif %}

  {% for field in form.visible_fields() %}
    {{ form_row_html(field) }}
  {% endfor %}

  {% for field in form.hidden_fields() %}
    {{ field|safe }}
  {% endfor %}

{% endmacro %}


{% macro form_html(form, extra_classes='', extra_attrs=none) %}
  <form method="POST" class="{{ extra_classes }}" role="form"{{ utils.html_attrs(extra_attrs) if extra_attrs }}{{ ' enctype="multipart/form-data"'|safe if form.is_multipart() }}>
    {{ form_body_html(form) }}
    <button type="submit" class="btn btn-primary">Submit</button>
  </form>
{% endmacro %}