# Generated by Django 4.1.5 on 2023-01-18 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ideas", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="idea",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="ideas/%Y%m%d"),
        ),
    ]
