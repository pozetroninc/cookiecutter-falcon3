from falcon.testing import TestClient
import pytest

from {{cookiecutter.project_slug}}.app import wsgi_app


@pytest.fixture
def client():
    return TestClient(wsgi_app)
