# Generated by Django 4.1.3 on 2022-12-02 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_message_phonenumber_alter_message_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='score',
        ),
        migrations.AlterField(
            model_name='message',
            name='phonenumber',
            field=models.CharField(max_length=100),
        ),
    ]
