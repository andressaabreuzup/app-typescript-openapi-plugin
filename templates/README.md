
You can use jinja to make a template-data folder more dynamic.

complete documentation of jinja: https://jinja.palletsprojects.com/en/3.0.x/templates/

# Somes examples
## Variable

to inject some variable on the text use: "{{ example }}"
you can apply some filters to the variable example:
"{{ example|lower}}"
"{{ inputs.example|upper}}"
"{{ inputs.example|capitalize}}"

list of filters: https://jinja.palletsprojects.com/en/3.0.x/templates/#builtin-tests

## Ifs
{% if inputs.any_number > 5 %}
    log.printf("{{inputs.any_number}} is > 5 ")
{% else %}
    log.printf("{{inputs.any_number}} is <= 5 ")
{% endif %}

## For and List

{% for n in range(0, inputs.any_number) %}
    log.printf("Hello World {{n}}")
{% endfor %}

{% for item in inputs.any_list %}
    log.printf("{{item}}")
{% endfor %}

{% for item in inputs.any_list %}
    log.printf("index: {{loop.index0}}")
{% endfor %}

log.printf("{{inputs.any_list[0]}}")

## Commented
{# note: commented-out template because we no longer use this
    {% for user in users %}
        ...
    {% endfor %}
#}

## Folder names

Folder can have dynamic names examples folder with name "{{ inputs.example }}" will be replace by the input with name
"example".

