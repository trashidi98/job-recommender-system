from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import UserResume, BestJobsOutput, Endpoint, MLAlgorithm, MLAlgorithmStatus, MLRequest

admin.site.site_head = "AA10: Machine Learning for a Job Recommender System"
admin.site.site_title = "AA10 Database Admin Area"
admin.site.index_title = "Welcome to AA10 Database Admin Area!!"

# Register your models here.
# @admin.register(UserResume)
# class UserResumeAdmin(ImportExportModelAdmin):
#     model = UserResume
#     list_display = ("id", "user_resume",)

@admin.register(BestJobsOutput)
class BestJobsOutputAdmin(ImportExportModelAdmin):
    model = BestJobsOutput
    list_display = ("job_id", "job_title", "job_category", "company_name", "inferred_city", "inferred_state", "inferred_country", "job_description", "job_type", "similarity_score")

@admin.register(Endpoint)
class EndpointAdmin(ImportExportModelAdmin):
    model = Endpoint
    list_display = ("id", "name", "owner", "created_at")

@admin.register(MLAlgorithm)
class MLAlgorithmAdmin(ImportExportModelAdmin):
    model = MLAlgorithm
    list_display = ("id", "name", "description", "code","version", "owner", "created_at","parent_endpoint")

@admin.register(MLAlgorithmStatus)
class MLAlgorithmStatusAdmin(ImportExportModelAdmin):
    model = MLAlgorithmStatus
    list_display = ("id", "active", "status", "created_by", "created_at","parent_mlalgorithm")

@admin.register(MLRequest)
class MLRequestAdmin(ImportExportModelAdmin):
    model = MLRequest
    list_display = ("id","input_data","full_response","response","feedback","created_at","parent_mlalgorithm")