# Generated by Django 4.1.3 on 2022-12-02 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_message_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='phonenumber',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='message',
            name='score',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
