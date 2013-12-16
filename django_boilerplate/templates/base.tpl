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

    <link href="//ajax.googleapis.com/ajax/libs/jqueryui/1.10.3/themes/smoothness/jquery-ui.css" rel="stylesheet">
    {% compressed_css 'main' %}
    {% block extra_styles %}{% endblock %}

    <script>
      BOOT = {
        env: '{{ ENV }}',
        rel: {{ RELEASE_NUM }},
        staticUrl: '{{ STATIC_URL }}'
      };

      {% if DEBUG %}DEBUG = 1;{% endif -%}
    </script>

    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
    <script src="//ajax.googleapis.com/ajax/libs/jqueryui/1.10.3/jquery-ui.js"></script>
    {% compressed_js 'main' %}
    {% block extra_scripts %}{% endblock %}
    <script>
      $(function() {
        window.app = new App.controllers.App();
      });
    </script>

    {% if not PIPELINE_ENABLED %}
    <script>
      var less = { env: 'development' };
    </script>
    <script src="{% static 'third_party/less.js' %}"></script>
    {% endif %}

  </head>
  <body class="{% block body_class %}{% endblock %}">
    {% include 'djbp/includes/google_tag_manager.tpl' with context %}
    <div data-django-hijax-content>
      {% block body %}{% endblock %}
    </div>
    <div id="app-spinner"></div>
  </body>
</html>
{% endif %}