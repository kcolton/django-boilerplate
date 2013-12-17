{% if IS_BARE %}
  {% extends 'base_bare.tpl' %}
{% else %}
<!DOCTYPE html>
<!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js"> <!--<![endif]-->
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">

    <title>{{ TITLE }}</title>
    <meta name="viewport" content="width=device-width">

    {% include "djbp/includes/assets_early.tpl" %}

  </head>
  <body class="{% block body_class %}{% endblock %}">
    {% include 'djbp/includes/google_tag_manager.tpl' with context %}
    <div data-django-hijax-content>
      {% block body %}{% endblock %}
    </div>
    <div id="app-spinner"></div>
    {% include "djbp/includes/assets_late.tpl" %}
    <script>
      $(function() {
        window.app = new App.controllers.App();
      });
    </script>
  </body>
</html>
{% endif %}