# Generated by Django 5.1.2 on 2024-11-07 16:55

import boards.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_boardbutton_button_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardbutton',
            name='button_image',
            field=models.ImageField(null=True, upload_to=boards.models.user_directory_path),
        ),
    ]
