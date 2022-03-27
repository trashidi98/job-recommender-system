# backend/server/apps/endpoints/views.py file
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import permissions 
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from apps.ml.rs.computations import bestjobs_computations

from apps.endpoints.models import UserResume
from apps.endpoints.serializers import UserResumeSerializer

from apps.endpoints.models import Endpoint
from apps.endpoints.serializers import EndpointSerializer

from apps.endpoints.models import MLAlgorithm
from apps.endpoints.serializers import MLAlgorithmSerializer

from apps.endpoints.models import MLAlgorithmStatus
from apps.endpoints.serializers import MLAlgorithmStatusSerializer

def front(request):
    context = { }
    return render(request, "index.html", context)

class UserResumeViewSet(generics.ListCreateAPIView):
    
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head', 'post']

    def get(self, request, *args, **kwargs):
        serializer = UserResumeSerializer(UserResume.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):        
        serializer = self.get_serializer(data=request.data)   
        prediction = bestjobs_computations(request.data["resume_text"], request.data["city"]) 
        serializer.is_valid(raise_exception=True)
        serializer.validated_data
        print(serializer.validated_data)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(prediction, status=status.HTTP_201_CREATED, headers=headers)
        
class EndpointViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = EndpointSerializer
    queryset = Endpoint.objects.all()

class MLAlgorithmViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = MLAlgorithmSerializer
    queryset = MLAlgorithm.objects.all()

def deactivate_other_statuses(instance):
    old_statuses = MLAlgorithmStatus.objects.filter(parent_mlalgorithm = instance.parent_mlalgorithm,
                                                        created_at__lt=instance.created_at,
                                                        active=True)
    for i in range(len(old_statuses)):
        old_statuses[i].active = False
    MLAlgorithmStatus.objects.bulk_update(old_statuses, ["active"])

class MLAlgorithmStatusViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet,mixins.CreateModelMixin):
    serializer_class = MLAlgorithmStatusSerializer
    queryset = MLAlgorithmStatus.objects.all()
    def perform_create(self, serializer):
        try:
            with transaction.atomic():
                instance = serializer.save(active=True)
                # set active=False for other statuses
                deactivate_other_statuses(instance)

        except Exception as e:
            raise APIException(str(e))
