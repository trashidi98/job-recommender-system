from django.test import TestCase

# Create your tests here.
from apps.ml.rs.training import RecommenderSystem

class MLTests(TestCase):
    def test_rf_algorithm(self):
        
        my_alg = RecommenderSystem()
        response = my_alg.test()
        #self.assertEqual('OK', response)