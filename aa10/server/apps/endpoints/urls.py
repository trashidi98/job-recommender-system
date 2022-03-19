# backend/server/apps/endpoints/urls.py file
from django.urls import re_path as url, include
from rest_framework.routers import DefaultRouter

from apps.endpoints.views import EndpointViewSet
from apps.endpoints.views import MLAlgorithmViewSet
from apps.endpoints.views import MLAlgorithmStatusViewSet
from apps.endpoints.views import MLRequestViewSet
from apps.endpoints.views import PredictView # import PredictView
from apps.endpoints.views import BestJobsOutputViewSet

router = DefaultRouter(trailing_slash=False)
router.register("endpoints", EndpointViewSet, basename="endpoints")
router.register("mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register("mlalgorithmstatuses", MLAlgorithmStatusViewSet, basename="mlalgorithmstatuses")
router.register("mlrequests", MLRequestViewSet, basename="mlrequests")
router.register("bestjobs", BestJobsOutputViewSet, basename="bestjobs")

urlpatterns = [
    url("api/v1/", include(router.urls)),
     # add predict url
    url("predict", PredictView.as_view(), name="predict")
]