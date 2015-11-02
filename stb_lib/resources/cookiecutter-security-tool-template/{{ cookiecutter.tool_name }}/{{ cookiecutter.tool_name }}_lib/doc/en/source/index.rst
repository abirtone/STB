.. Documentation master file, created by
   sphinx-quickstart on Wed Feb 11 01:21:33 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to {{ cookiecutter.tool_name }} documentation!
==========={% for x in range((cookiecutter.tool_name|length)) %}={% endfor %}===============

What's {{ cookiecutter.tool_name }}
-------{% for x in range((cookiecutter.tool_name|length)) %}-{% endfor %}

{{ cookiecutter.brief_description }}

Author
------

{{ cookiecutter.tool_name }} was written by {{ cookiecutter.author }}.

Project site
------------

Sources and URL of project in:

{{ cookiecutter.project_site }}

Content Index
-------------

.. toctree::
   :maxdepth: 2

   advanced