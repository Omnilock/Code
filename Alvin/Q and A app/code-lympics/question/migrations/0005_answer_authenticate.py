# Generated by Django 2.1.5 on 2019-02-21 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0004_auto_20070101_0156'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='authenticate',
            field=models.BooleanField(default=False),
        ),
    ]
