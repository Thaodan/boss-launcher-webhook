# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-30 13:06


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170329_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webhookmapping',
            name='project',
            field=models.CharField(help_text=b'name of an existing project under which to create or update the package', max_length=250),
        ),
    ]
