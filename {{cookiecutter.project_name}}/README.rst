{{ cookiecutter.project_name }}
==============================

{{ cookiecutter.project_description }}

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django

{% if cookiecutter.open_source_license != "Not open source" %}
LICENSE: {{ cookiecutter.open_source_license }}
{% endif %}

Deployment
----------
Local
^^^^^

To deploy the app locally (for testing/development), you will need to:
#. Create a virtualenv (basic).
#. Install application package as develop.
   .. code-block:: bash
        python setup.py develop
#. Serve the application itself:
   .. code-block:: bash
        export FALCON_SETTINGS_MODULE={{cookiecutter.project_slug}}.settings.local
        python {{ cookiecutter.project_slug }}/run_bjoern.py

   Or

   .. code-block:: bash
        export FALCON_SETTINGS_MODULE={{cookiecutter.project_slug}}.settings.local
        python {{ cookiecutter.project_slug}}/app.py

It is very important to set the environment before serving the app or it won't work.

{% if cookiecutter.use_docker == "y" %}

Docker
^^^^^^

To run the docker containerized application you just need to run:

.. code-block:: bash
    $ docker-compose up --build

To build and push the containerized container you first need to update the `Makefile`
with the correct values for `NS = [DOCKER_REGISTRY]/[PROJECT-ID]`

e.g.
.. code-block:: bash
    NS = gcr.io/my_project
or for the Docker Hub
.. code-block:: bash
    NS = [hub_user]

{% endif %}
