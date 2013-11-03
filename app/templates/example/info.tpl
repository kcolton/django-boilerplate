{% extends "example/body.tpl" %}

{% block content %}
<h1>Request Info</h1>
<pre>
  {{ request|pprint }}
</pre>
{% endblock %}