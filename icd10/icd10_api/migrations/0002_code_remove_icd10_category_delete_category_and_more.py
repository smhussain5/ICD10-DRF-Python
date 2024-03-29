# Generated by Django 4.2.7 on 2024-02-11 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icd10_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icd10_code', models.CharField(max_length=3, verbose_name='ICD-10 Code')),
                ('category', models.CharField(max_length=1000, verbose_name='ICD-10 Category')),
                ('diagnosis', models.CharField(max_length=1000, verbose_name='ICD-10 Diagnosis')),
            ],
            options={
                'verbose_name_plural': 'ICD-10 Codes',
            },
        ),
        migrations.RemoveField(
            model_name='icd10',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='ICD10',
        ),
    ]
