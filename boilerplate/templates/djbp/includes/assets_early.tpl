{% if JQUERY_UI %}
  {% if CDN_LIBRARIES %}
    <link href="//ajax.googleapis.com/ajax/libs/jqueryui/1.10.3/themes/smoothness/jquery-ui.css" rel="stylesheet">
  {% else %}
    <link href="{% static 'third_party/jqueryui/1.10.3/themes/base/jquery-ui.css' %}" rel="stylesheet">
  {% endif %}
{% endif %}

{% compressed_css 'main' %}

{% if not PIPELINE_ENABLED %}
<script>
  var less = { env: 'development' };
</script>
<script src="{% static 'third_party/less.js' %}"></script>
{% endif %}