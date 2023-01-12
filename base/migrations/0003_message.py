# Generated by Django 4.1.3 on 2022-12-02 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
    ]
