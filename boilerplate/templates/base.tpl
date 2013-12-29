{% if IS_BARE %}
  {% extends 'base_bare.tpl' %}
{% else %}
<!DOCTYPE html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js"> <!--<![endif]-->
  <head>
    {% block head_top %}{% endblock %}
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">

    <title>{{ TITLE }}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    {% include "djbp/includes/assets_early.tpl" with context %}

    {% block head_bottom %}{% endblock %}
  </head>
  <body class="{% block body_class %}{% endblock %}">
    {% block body_top %}{% endblock %}
    <div data-app-page>
      {% block body %}{% endblock %}
    </div>
    <div id="app-spinner"></div>
    {% include "djbp/includes/assets_late.tpl" with context %}
    <script>
      $(function() {
        window.app = new App.controllers.App($('[data-app-page]'));
      });
    </script>
    {% include 'djbp/includes/google_tag_manager.tpl' with context %}
    {% block body_bottom %}{% endblock %}
  </body>
</html>
{% endif %}