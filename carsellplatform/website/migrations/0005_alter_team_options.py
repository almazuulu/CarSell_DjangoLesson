# Generated by Django 4.1.6 on 2023-03-15 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0004_alter_team_photo"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="team",
            options={
                "ordering": ["-created_date"],
                "verbose_name": "Worker",
                "verbose_name_plural": "Workers",
            },
        ),
    ]
