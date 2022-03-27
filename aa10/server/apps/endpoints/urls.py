# backend/server/apps/endpoints/urls.py file
from django.urls import re_path as url, include
from rest_framework.routers import DefaultRouter

from apps.endpoints.views import EndpointViewSet
from apps.endpoints.views import MLAlgorithmViewSet
from apps.endpoints.views import MLAlgorithmStatusViewSet
from apps.endpoints.views import UserResumeViewSet

from apps.endpoints.models import UserResume
from apps.endpoints.serializers import UserResumeSerializer

router = DefaultRouter(trailing_slash=False)
router.register("endpoints", EndpointViewSet, basename="endpoints")
router.register("mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register("mlalgorithmstatuses", MLAlgorithmStatusViewSet, basename="mlalgorithmstatuses")

urlpatterns = [
    
    url("api/v1/userresume", UserResumeViewSet.as_view(queryset = UserResume.objects.all(), serializer_class = UserResumeSerializer), name='userresume'),
    url("api/v1/", include(router.urls)),
]