# Generated by Django 5.0.6 on 2024-05-27 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_view_course_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
