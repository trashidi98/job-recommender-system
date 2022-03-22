# backend/server/apps/endpoints/serializers.py file
from rest_framework import serializers
from apps.endpoints.models import Endpoint
from apps.endpoints.models import MLAlgorithm
from apps.endpoints.models import MLAlgorithmStatus
from apps.endpoints.models import MLRequest
from apps.endpoints.models import BestJobsOutput
from apps.endpoints.models import UserResume


class UserResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserResume
        #read_only_fields = ("resume_text")
        fields = ("resume_text", )
        def create(self, validated_data):
            my_incoming_data = validated_data
            # If you want to pop any field from the incoming data then you can like below.
            # popped_data = validated_data.pop('timeFrames')
            inserted_data = UserResume.objects.create(**validated_data)
            return Response(inserted_data)


class BestJobsOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestJobsOutput
        read_only_fields = ("job_id", "job_title", "job_category", "company_name", "inferred_city", "inferred_state", "inferred_country", "job_description", "job_type")
        fields = ("job_id", "job_title", "job_category", "company_name", "inferred_city", "inferred_state", "inferred_country", "job_description", "job_type", "similarity_score")

class EndpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endpoint
        read_only_fields = ("id", "name", "owner", "created_at")
        fields = read_only_fields

class MLAlgorithmSerializer(serializers.ModelSerializer):
    current_status = serializers.SerializerMethodField(read_only=True)
    def get_current_status(self, mlalgorithm):
        return MLAlgorithmStatus.objects.filter(parent_mlalgorithm=mlalgorithm).latest('created_at').status
    class Meta:
        model = MLAlgorithm
        read_only_fields = ("id", "name", "description", "code","version", "owner", "created_at","parent_endpoint", "current_status")
        fields = read_only_fields

class MLAlgorithmStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLAlgorithmStatus
        read_only_fields = ("id", "active")
        fields = ("id", "active", "status", "created_by", "created_at","parent_mlalgorithm")

class MLRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLRequest
        read_only_fields = ("id","input_data","full_response","response","created_at","parent_mlalgorithm")
        fields =  ("id","input_data","full_response","response","feedback","created_at","parent_mlalgorithm",)