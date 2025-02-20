# Generated by Django 5.0.7 on 2024-07-29 12:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_applyform_careerinfo_alter_contactdata_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='StepformData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, null=True)),
                ('Email', models.EmailField(max_length=50, null=True)),
                ('Phone', models.CharField(max_length=10, null=True)),
                ('Brandmarketposition', models.CharField(max_length=100)),
                ('BrandCorevalue', models.CharField(max_length=500)),
                ('Brandperceive_targetaudience', models.CharField(max_length=100)),
                ('CustomerFeedback', models.CharField(max_length=100)),
                ('BrandPerformence', models.CharField(max_length=500)),
                ('Challenges_Obstacles', models.CharField(max_length=500)),
                ('Brand_Motivation', models.CharField(max_length=500)),
                ('Goals_Achieves', models.CharField(max_length=500)),
                ('Expectations', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='contactdata',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 29, 17, 59, 18, 317786)),
        ),
    ]
