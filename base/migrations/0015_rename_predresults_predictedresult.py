# Generated by Django 4.1.5 on 2023-01-25 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_resultmail_result'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PredResults',
            new_name='PredictedResult',
        ),
    ]
