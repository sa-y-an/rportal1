# Generated by Django 3.2.4 on 2021-07-27 09:03

import django.core.validators
from django.db import migrations, models
import usr_val.models


class Migration(migrations.Migration):

    dependencies = [
        ('usr_val', '0010_auto_20210727_0331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.CharField(blank=True, choices=[('BT', 'BT'), ('CE', 'CE'), ('CH', 'CH'), ('CS', 'CH'), ('CY', 'CY'), ('EC', 'EC'), ('EE', 'EE'), ('ES', 'ES'), ('HS', 'HS'), ('MA', 'MA'), ('ME', 'ME'), ('MM', 'MM'), ('MS', 'MS'), ('PH', 'PH')], max_length=4),
        ),
        migrations.AlterField(
            model_name='student',
            name='cv',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to=usr_val.models.cv_upload_location, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='branch',
            field=models.CharField(blank=True, choices=[('BT', 'BT'), ('CE', 'CE'), ('CH', 'CH'), ('CS', 'CH'), ('CY', 'CY'), ('EC', 'EC'), ('EE', 'EE'), ('ES', 'ES'), ('HS', 'HS'), ('MA', 'MA'), ('ME', 'ME'), ('MM', 'MM'), ('MS', 'MS'), ('PH', 'PH')], max_length=4),
        ),
    ]
