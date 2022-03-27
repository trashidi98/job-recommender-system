from django.test import TestCase
import inspect
from apps.ml.registry import MLRegistry
from apps.ml.rs.training import RecommenderSystem

# ...
# the rest of the code
# ...
class MLTests(TestCase):

# add below method to MLTests class:
    def test_registry(self):
        registry = MLRegistry()
        self.assertEqual(len(registry.endpoints), 0)
        endpoint_name = "rs"
        algorithm_object = RecommenderSystem()
        algorithm_name = "random forest"
        algorithm_status = "production"
        algorithm_version = "0.0.1"
        algorithm_owner = "Saima"
        algorithm_description = "Recommender System with pre- and post-processing"
        algorithm_code = inspect.getsource(RecommenderSystem)
        # add to registry
        registry.add_algorithm(endpoint_name, algorithm_object, algorithm_name,
                    algorithm_status, algorithm_version, algorithm_owner,
                    algorithm_description, algorithm_code)
        # there should be one endpoint available
        self.assertEqual(len(registry.endpoints), 1)