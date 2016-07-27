{{ cookiecutter.tool_name }}
{% for x in range((cookiecutter.tool_name|length)) %}={% endfor %}


![Logo](https://raw.githubusercontent.com/abirtone/STB/master/stb_lib/doc/images/logo.png)

*{{ cookiecutter.tool_name }}: {{ cookiecutter.brief_description }}*

Code | {{ cookiecutter.project_site }}
---- | ----------------------------------------------
Issues | {{ cookiecutter.project_site }}/issues/
{%- if cookiecutter.python_version_3 %}
    {%- set run_python_version_3 = "3" %}
{%- endif %}
{%- if cookiecutter.python_version_2 %}
    {%- set run_python_version_2 = "2" %}
{%- endif %}

{%- if cookiecutter.python_version_3 == "3" and cookiecutter.python_version_2 == "2" %}
    {%- set run_python_version_sep = " & " %}
{%- else %}
    {%- set run_python_version_sep = "" %}
{%- endif %}
Python version | Python {{ run_python_version_3 }}{{ run_python_version_sep }}{{ run_python_version_2 }}

What's {{ cookiecutter.tool_name }}
-------{% for x in range((cookiecutter.tool_name|length)) %}-{% endfor %}

{{ cookiecutter.long_description }}

What's new?
-----------

This {{ cookiecutter.tool_name }} version, add a lot of new features and fixes, like:

Version {{ cookiecutter.project_version }}
++++++++{% for x in range((cookiecutter.project_version|length)) %}+{% endfor %}

- First version released

You can read entire list in CHANGELOG file.

Installation
------------

Install {{ cookiecutter.tool_name }} is so easy:

```
$ python -m pip install {{ cookiecutter.tool_name }}
```

{%- if cookiecutter.python_version_3 != cookiecutter.python_version_2 %}
    {%- if cookiecutter.python_version_3 %}
        {%- set run_python_version = 3 %}
    {%- else %}
        {%- set run_python_version = 2 %}
    {%- endif %}

**Remember that {{ cookiecutter.tool_name }} only runs in Python {{ run_python_version }}**.
{%- endif %}

Quick start
-----------

You can display inline help writing:

```bash

python {{ cookiecutter.tool_name }}.py -h
```

Advanced options
----------------

There are the advanced options:

- **-v**, **-vv**, **-vvv**: Enable verbose mode.

References
----------

* OMSTD (Open Methodology for Security Tool Developers): http://omstd.readthedocs.org
* STB (Security Tool Builder): https://github.com/abirtone/STB 
