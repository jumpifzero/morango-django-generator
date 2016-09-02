from django.db import models

{% macro field(f) -%}
{%- if f.type == 'Boolean' -%}
models.BooleanField()
{%- elif f.type == 'String' or f.type == 'Text' %}
models.CharField(max_length=30)
{%- elif f.type == 'Integer' %}
models.IntegerField()
{%- elif f.type == 'Decimal' or f.type == 'Float' %}
models.{{f.type}}Field()
{%- elif f.type == 'File' %}
models.FileField()
{%- elif f.type == 'Image' %}
models.ImageField()
{%- elif f.type == 'Audio' %}
{%- elif f.type == 'Date' %}
models.DateField()
{%- elif f.relationship %}
models.CharField(max_length=30)
{%- endif %}
{%- endmacro %}



{% for m in models %}
class {{m.name}}(models.Model):
	{% for f in m.fields %}
  {{f.name}} = {{field(f)}}
	{% endfor %}

{% endfor %}
