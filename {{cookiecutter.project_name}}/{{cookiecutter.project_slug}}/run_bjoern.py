import bjoern
from app import wsgi_app

bjoern.run(wsgi_app, '0.0.0.0', 8000)
