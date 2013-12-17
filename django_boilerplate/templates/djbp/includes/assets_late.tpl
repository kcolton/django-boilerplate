{% if CDN_LIBRARIES %}
  <script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
{% else %}
  <script src="{% static 'third_party/jquery/1.10.2/jquery.js' %}"></script>
{% endif %}

{% if JQUERY_UI %}
  {% if CDN_LIBRARIES %}
    <script src="//ajax.googleapis.com/ajax/libs/jqueryui/1.10.3/jquery-ui.js"></script>
  {% else %}
    <script src="{% static 'third_party/jqueryui/1.10.3/jquery-ui.js' %}"></script>
  {% endif %}
{% endif %}

{% if LODASH %}
  {% if CDN_LIBRARIES %}
    <script src="//cdnjs.cloudflare.com/ajax/libs/lodash.js/2.3.0/lodash.min.js"></script>
  {% else %}
    <script src="{% static 'third_party/lodash/2.3.0/lodash.min.js' %}"></script>
  {% endif %}
{% endif %}

{% compressed_js 'main' %}