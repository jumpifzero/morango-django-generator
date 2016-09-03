{# The following macro generates the django field definition #}
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
{%- elif f.type == 'Email' %}
models.EmailField()
{%- elif f.relationship %}
models.ManyToManyField('{{f.type}}', blank={{f.multiplicity.min==0}})
{%- else %}
Bug in the generator. Unsupported field type!
{%- endif %}
{%- endmacro %}
from django.db import models


{% for m in models %}
class {{m.name}}(models.Model):
	{% for f in m.fields %}
	{{f.name}} = {{field(f)}}
	{% endfor %}

{% endfor %}


