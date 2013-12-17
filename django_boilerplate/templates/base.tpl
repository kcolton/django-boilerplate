{% if IS_BARE %}
  {% extends 'base_bare.tpl' %}
{% else %}
<!DOCTYPE html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js"> <!--<![endif]-->
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">

    <title>{{ TITLE }}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    {% include "djbp/includes/assets_early.tpl" with context %}
  </head>
  <body class="{% block body_class %}{% endblock %}">
    <div data-django-hijax-content>
      {% block body %}{% endblock %}
    </div>
    <div id="app-spinner"></div>
    {% include "djbp/includes/assets_late.tpl" with context %}
    <script>
      $(function() {
        window.app = new App.controllers.App();
      });
    </script>
    {% include 'djbp/includes/google_tag_manager.tpl' with context %}
  </body>
</html>
{% endif %}