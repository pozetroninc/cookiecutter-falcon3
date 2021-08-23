# Cookiecutter Falcon 3.0

This guide should get you started with [Falcon 3.0 ](https://github.com/falconry/falcon) projects quickly by using the wonderful cookicutter.

It will set up an simple WSGI app as well as an ASGI app. Both versions include a simple health check listening for get requests to `/healthz/`. The ASGI version also includes an example of how to implement WebSockets with Falcon. To ensure the resulting projects are blazingly fast this template utilizes [Bjoern](https://github.com/jonashaag/bjoern) for the WSGI server and [Uvicorn](https://github.com/encode/uvicorn) for ASGI.

### Cookiecutter
Cookiecutter is a command-line utility that creates projects from cookiecutters (project templates), e.g. creating a Python package project from a Python package project template.

### Install cookiecutter
It's simple, you only need to install python package:
```
pip install cookiecutter
```
Now you can create new projects using your new favourite template.

### Get the template
You need to clone the git repository:
```
git clone https://github.com/pozetroninc/cookiecutter-falcon3.git
```

### Create skeleton
To create the skeleton you need to indicate to cookiecutter where the template is:
```bash
cookiecutter cookiecutter-falcon3/
```

The tool is interactive and it will request for some information as:
* project_name
* project_slug
* author_name
* author_mail
* project_description [A short description of the project.]
* project_url [example.com]
* use_docker
* use_mongodb
* use_redisdb
* Select open_source_license or not open source

Note: The project_name should not contain spaces or other characters which aren't valid directory names.

When finished, a folder in the current directory with the name of selected "project_name" step given is created. You only need to move it where you want it lives:

```
cd my-project
tree .
.
├── my-project
│   ├── app.py
│   ├── __init__.py
│   ├── run_bjoern.py
│   ├── run_uvicorn.py
│   ├── healthcheck
│   │   ├── __init__.py
│   │   └── healthz.py
│   ├── sample
│   │   ├── __init__.py
|   |   ├── websocket.py
│   │   └── models.py
│   └── settings
│       ├── base.py
│       ├── docker.py
│       ├── __init__.py
│       ├── local.py
│       └── production.py
├── docker
│   ├── falcon-bjoern-entrypoint.sh
|   ├── falcon-uvicorn-entrypoint.sh
│   └── FalconDockerfile
├── docker-compose.yml
├── README.rst
├── requirements
│   ├── dev-requirements.txt
│   ├── requirements.txt
│   └── test-requirements.txt
├── setup.py
└── tox.ini

5 directories, 18 files
```

Note: This project is a fork of the original project for Falcon 1.0 projects at https://github.com/7ideas/cookiecutter-falcon
