# Generated by Django 4.1.6 on 2023-02-06 15:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Team",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("designation", models.CharField(max_length=255)),
                ("facebook_link", models.URLField(blank=True, max_length=255)),
                ("twitter_link", models.URLField(blank=True, max_length=255)),
                ("whatsapp_link", models.URLField(blank=True, max_length=255)),
                ("created_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
