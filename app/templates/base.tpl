<!DOCTYPE html>
<!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js"> <!--<![endif]-->
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">

    <title>{% block full_title %}{% block title %}{% endblock %} | ACME{% endblock %}</title>
    <meta name="viewport" content="width=device-width">

    {% if ENV == 'local' %}
    <script src="{{ 'js/ext/jquery/jquery.js'|static }}"></script>
    {% else %}
    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
    {% endif %}

    <script>
      BOOT = {
        env: '{{ ENV }}',
        rel: {{ RELEASE_NUM }},
        staticUrl: '{{ STATIC_URL }}'
      };
      
      {% if DEBUG %}DEBUG = 1;{% endif -%}
    </script>

    {% assets "main.js" %}<script src="{{ ASSET_URL }}"></script>
    {% endassets %}

    {% assets "main.css" %}<link rel="{{ EXTRA.rel }}" type="text/css" href="{{ ASSET_URL }}" />
    {% endassets %}

    {% if ASSETS_DEBUG %}
    <script>
      var less = { env: 'development' };
    </script>
    <script src="{{ 'js/ext/less.js'|static }}"></script>
    {% endif %}

    {% block seo_tags %}{% endblock %}
    {% block head_tags %}{% endblock %}
  </head>
  <body class="{% block body_class %}{% endblock %}">
    {% block content %}{% endblock %}
  </body>
</html>
