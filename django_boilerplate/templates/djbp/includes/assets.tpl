{% if JQUERY_UI %}
  {% if CDN_LIBRARIES %}
    <link href="//ajax.googleapis.com/ajax/libs/jqueryui/1.10.3/themes/smoothness/jquery-ui.css" rel="stylesheet">
  {% else %}
    <link href="{% static 'third_party/jqueryui/1.10.3/themes/smoothness/jquery-ui.css' %}" rel="stylesheet">
  {% endif %}
{% endif %}

{% compressed_css 'main' %}
{% block extra_styles %}{% endblock %}


{% if CDN_LIBRARIES %}
  <script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
{% else %}
  <script src="{% static 'third_party/jquery/1.10.2/jquery.js' %}"></script>
{% endif %}

{% if JQUERY_UI %}
  {% if CDN_LIBRARIES %}
    <script src="//ajax.googleapis.com/ajax/libs/jqueryui/1.10.3/jquery-ui.js"></script>
  {% else %}
    <script src"{% static 'third_party/jqueryui/1.10.3/jquery-ui.js' %}"></script>
  {% endif %}
{% endif %}

{% compressed_js 'main' %}
{% block extra_scripts %}{% endblock %}


{% if not PIPELINE_ENABLED %}
<script>
  var less = { env: 'development' };
</script>
<script src="{% static 'third_party/less.js' %}"></script>
{% endif %}