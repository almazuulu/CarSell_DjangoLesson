# Generated by Django 4.1.6 on 2023-02-10 14:33

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0002_alter_car_car_main_photo"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="car", options={"ordering": ["created_date"]},
        ),
        migrations.AlterField(
            model_name="car", name="description", field=ckeditor.fields.RichTextField(),
        ),
    ]