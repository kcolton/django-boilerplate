{# Inspired by: https://github.com/tzangms/django-bootstrap-form/ #}

{% import "djbp/macros/utils.tpl" as utils %}


{% macro input_helpers(form_field) %}
  {% for error in form_field.errors %}
    <span class="help-block">{{ error }}</span>
  {% endfor %}

  {% if form_field.help_text %}
    <p class="help-block">{{ form_field.help_text|safe }}</p>
  {% endif %}
{% endmacro %}


{% macro input_checkbox(form_field) %}
  <div class="checkbox">
    <label>{{ form_field|safe }} {{ form_field.label }}</label>
  </div>
{% endmacro %}


{% macro input_radio(form_field) %}
  {% for choice in form_field %}
    <div class="radio">
      <label>{{ choice.tag()|safe }} {{ choice.choice_label }}</label>
    </div>
  {% endfor %}
{% endmacro %}


{% macro input_checkbox_multiple(form_field) %}
  {{ form_field|safe }}
{% endmacro %}


{% macro input_datetime(form_field, datetime_col='col-sm-6 col-md-4') %}
  {% set dt = form_field.value()|parsedatetime if form_field.value() is string else form_field.value() %}

  <div data-app-datetime-field="{{ form_field.auto_id }}"{{ ' class="has-error"' if form_field.errors }}>
    <div class="{{ datetime_col }} form-group">
      <input type="hidden" name="{{ form_field.name }}" id="{{ form_field.auto_id }}" value="{{ dt|date('Y-m-d H:i') if dt }}" data-app-datetime>

      <div class="input-group">
        <input type="text" class="form-control" data-app-datetime-date data-app-datepicker
               name="{{ form_field.name }}_date" id="{{ form_field.auto_id }}_date"
               value="{{ dt|date('m/d/Y') if dt }}">

        <span class="input-group-addon" data-app-datepicker="#{{ form_field.auto_id }}_date">
          <span class="glyphicon glyphicon-calendar"></span>
        </span>
      </div>
    </div>
    <div class="{{ datetime_col }} form-group">
      <div class="input-group">
        <input type="text" class="form-control" placeholder="12:00 AM" data-app-datetime-time
               name="{{ form_field.name }}_time" id="{{ form_field.auto_id }}_time"
               value="{{ dt|date('h:i A') if dt }}">

        <span class="input-group-addon">
          <span class="glyphicon glyphicon-time"></span>
        </span>
      </div>
    </div>
  </div>
{% endmacro %}


{% macro input_standard(form_field) %}
  {{ form_field|add_class('form-control')|safe }}
{% endmacro %}


{% macro input(form_field) %}

  {% if form_field|is_checkbox %}
    {{ input_checkbox(form_field) }}
  {% elif form_field|is_radio %}
    {{ input_radio(form_field) }}
  {% elif form_field|is_checkbox_multiple %}
    {{ input_checkbox_multiple(form_field) }}
  {% elif form_field|is_datetime %}
    {{ input_datetime(form_field) }}
  {% else %}
    {{ input_standard(form_field) }}
  {% endif %}

{% endmacro %}


{% macro field(form_field, label_col='col-md-4', input_col='col-md-8', datetime_col='col-sm-6 col-md-4', full_col='col-md-12') %}
  {# Look at the type of field widget to see how to render it #}

  {% if form_field|is_checkbox %}
    <div class="{{ label_col }}"></div>
    <div class="{{ input_col }} form-group{{ ' has-error' if form_field.errors }}">
      {{ input_checkbox(form_field) }}
      {{ input_helpers(form_field) }}
    </div>
  {% elif form_field|is_radio %}
    <div class="{{ label_col }}">
      {{ form_field.label_tag()|safe }}
    </div>
    <div class="{{ input_col }} form-group{{ ' has-error' if form_field.errors }}">
      {{ input_radio(form_field) }}
      {{ input_helpers(form_field) }}
    </div>
  {% elif form_field|is_checkbox_multiple %}
    {# Where is the bootstrapy HTML? Nowhere until django 1.6 lands and un-retards CheckboxSelectMultiple #}

    <div class="{{ label_col }}">
      {{ form_field.label_tag()|safe }}
    </div>
    <div class="{{ input_col }} form-group{{ ' has-error' if form_field.errors }}">
      {{ input_checkbox_multiple(form_field) }}
      {{ input_helpers(form_field) }}
    </div>
  {% elif form_field|is_datetime %}
    <div class="{{ label_col }}">
      {{ form_field.label_tag()|safe }}
    </div>
    {{ input_datetime(form_field, datetime_col) }}
    <div class="row">
      <div class="{{ label_col }}"></div>
      <div class="{{ input_col }}">{{ input_helpers(form_field) }}</div>
    </div>
  {% else %}
    <div class="{{ label_col }}">
      {{ form_field.label_tag()|safe }}
    </div>
    <div class="{{ input_col }} form-group{{ ' has-error' if form_field.errors }}">
      {{ input_standard(form_field) }}
      {{ input_helpers(form_field) }}
    </div>
  {% endif %}

{% endmacro %}


{% macro field_row(form_field, label_col='col-md-4', input_col='col-md-8', datetime_col='col-sm-6 col-md-4', full_col='col-md-12') %}
  <div class="row">
    {{ field(form_field, label_col, input_col, datetime_col, full_col) }}
  </div>
{% endmacro %}


{% macro non_field_errors(form) %}
  {% if form.non_field_errors() %}
    <div class="alert alert-danger">
      <a class="close" data-dismiss="alert">&times;</a>
      {% for non_field_error in form.non_field_errors() %}
        {{ non_field_error }}
      {% endfor %}
    </div>
  {% endif %}
{% endmacro %}


{% macro body(form, label_col='col-md-4', input_col='col-md-8', datetime_col='col-sm-6 col-md-4', full_col='col-md-12') %}
  {{ non_field_errors(form) }}

  {% for visible_field in form.visible_fields() %}
    {{ field_row(visible_field, label_col, input_col, datetime_col, full_col) }}
  {% endfor %}

  {% for hidden_field in form.hidden_fields() %}
    {{ hidden_field|safe }}
  {% endfor %}
{% endmacro %}


{% macro form(form, action='', extra_classes='', extra_attrs=none, label_col='col-md-4', input_col='col-md-8', datetime_col='col-sm-6 col-md-4', full_col='col-md-12') %}
  <form method="POST" action="{{ action }}" class="{{ extra_classes }}" role="form"{{ utils.html_attrs(extra_attrs) if extra_attrs }}{{ ' enctype="multipart/form-data"'|safe if form.is_multipart() }}>
    {{ body(form, label_col, input_col, datetime_col, full_col) }}
    <div class="row form-group">
      <div class="{{ label_col }}"></div>
      <div class="{{ input_col }}">
        <button type="submit" class="btn btn-primary">Submit</button>
      </div>
    </div>
  </form>
{% endmacro %}