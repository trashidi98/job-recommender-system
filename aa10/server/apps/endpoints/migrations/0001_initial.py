# Generated by Django 4.0.3 on 2022-03-19 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BestJobsOutput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.IntegerField(blank=True, null=True)),
                ('job_title', models.CharField(max_length=10000)),
                ('job_category', models.CharField(blank=True, max_length=10000, null=True)),
                ('company_name', models.CharField(blank=True, max_length=10000, null=True)),
                ('inferred_city', models.CharField(blank=True, max_length=10000, null=True)),
                ('inferred_state', models.CharField(blank=True, max_length=10000, null=True)),
                ('inferred_country', models.CharField(blank=True, max_length=10000, null=True)),
                ('job_description', models.CharField(max_length=10000)),
                ('job_type', models.CharField(blank=True, max_length=10000, null=True)),
                ('similarity_score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Endpoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('owner', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MLAlgorithm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=1000)),
                ('code', models.CharField(max_length=50000)),
                ('version', models.CharField(max_length=128)),
                ('owner', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('parent_endpoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endpoints.endpoint')),
            ],
        ),
        migrations.CreateModel(
            name='MLRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_data', models.CharField(max_length=10000)),
                ('full_response', models.CharField(max_length=10000)),
                ('response', models.CharField(max_length=10000)),
                ('feedback', models.CharField(blank=True, max_length=10000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('parent_mlalgorithm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endpoints.mlalgorithm')),
            ],
        ),
        migrations.CreateModel(
            name='MLAlgorithmStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=128)),
                ('active', models.BooleanField()),
                ('created_by', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('parent_mlalgorithm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status', to='endpoints.mlalgorithm')),
            ],
        ),
    ]