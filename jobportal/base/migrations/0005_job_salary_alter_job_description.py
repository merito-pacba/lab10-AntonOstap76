# Generated by Django 5.0.11 on 2025-01-23 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_job_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='salary',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(default=0),
        ),
    ]
