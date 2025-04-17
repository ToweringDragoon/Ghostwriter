# Generated manually to add GCP credential fields

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("commandcenter", "0033_auto_20241204_1810"),  # Replace with your actual previous migration
    ]

    operations = [
        migrations.AddField(
            model_name="cloudservicesconfiguration",
            name="gcp_project_id",
            field=models.CharField(
                max_length=255,
                default="your-project-id",
                verbose_name="GCP Project ID",
            ),
        ),
        migrations.AddField(
            model_name="cloudservicesconfiguration",
            name="gcp_private_key_id",
            field=models.CharField(
                max_length=255,
                default="your-private-key-id",
                verbose_name="GCP Private Key ID",
            ),
        ),
        migrations.AddField(
            model_name="cloudservicesconfiguration",
            name="gcp_private_key",
            field=models.TextField(
                default="your-private-key",
                verbose_name="GCP Private Key",
            ),
        ),
        migrations.AddField(
            model_name="cloudservicesconfiguration",
            name="gcp_client_email",
            field=models.CharField(
                max_length=255,
                default="your-service-account@project.iam.gserviceaccount.com",
                verbose_name="GCP Client Email",
            ),
        ),
        migrations.AddField(
            model_name="cloudservicesconfiguration",
            name="gcp_client_id",
            field=models.CharField(
                max_length=255,
                default="your-client-id",
                verbose_name="GCP Client ID",
            ),
        ),
        migrations.AddField(
            model_name="cloudservicesconfiguration",
            name="gcp_auth_uri",
            field=models.CharField(
                max_length=255,
                default="https://accounts.google.com/o/oauth2/auth",
                verbose_name="GCP Auth URI",
            ),
        ),
        migrations.AddField(
            model_name="cloudservicesconfiguration",
            name="gcp_token_uri",
            field=models.CharField(
                max_length=255,
                default="https://oauth2.googleapis.com/token",
                verbose_name="GCP Token URI",
            ),
        ),
        migrations.AddField(
            model_name="cloudservicesconfiguration",
            name="gcp_auth_cert_url",
            field=models.CharField(
                max_length=255,
                default="https://www.googleapis.com/oauth2/v1/certs",
                verbose_name="GCP Auth Provider Cert URL",
            ),
        ),
        migrations.AddField(
            model_name="cloudservicesconfiguration",
            name="gcp_client_cert_url",
            field=models.TextField(
                default="https://www.googleapis.com/robot/v1/metadata/x509/your-service-account@project.iam.gserviceaccount.com",
                verbose_name="GCP Client Cert URL",
            ),
        ),
    ]
