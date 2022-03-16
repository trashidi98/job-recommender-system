"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

application = get_wsgi_application()

# ML registry
import inspect
from apps.ml.registry import MLRegistry
from apps.ml.rs.training import RecommenderSystem

try:
    registry = MLRegistry() # create ML registry
    # Random Forest classifier
    rf = RecommenderSystem()
    # add to ML registry
    registry.add_algorithm(endpoint_name="rs",
                            algorithm_object=rf,
                            algorithm_name="RS",
                            algorithm_status="testing",
                            algorithm_version="0.0.1",
                            owner="Saima",
                            algorithm_description="RS with pre- and post-processing",
                            algorithm_code=inspect.getsource(RecommenderSystem))

except Exception as e:
    print("Exception while loading the algorithms to the registry,", str(e))