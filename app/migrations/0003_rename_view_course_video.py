# Generated by Django 5.0.6 on 2024-05-26 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_course_image_course_view_rename_courseorders_order_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='view',
            new_name='video',
        ),
    ]
