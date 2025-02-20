# Generated by Django 5.0.7 on 2024-12-03 11:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_intalksform_alter_contactdata_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='intalksform',
            old_name='Intalk_City',
            new_name='City',
        ),
        migrations.RenameField(
            model_name='intalksform',
            old_name='Intalk_Contact',
            new_name='Contact',
        ),
        migrations.RenameField(
            model_name='intalksform',
            old_name='Intalk_Email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='intalksform',
            old_name='Intalk_Name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='intalksform',
            old_name='Intalk_Reason_to_connect',
            new_name='Reason_to_connect',
        ),
        migrations.AlterField(
            model_name='contactdata',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 3, 16, 42, 51, 689861)),
        ),
    ]
