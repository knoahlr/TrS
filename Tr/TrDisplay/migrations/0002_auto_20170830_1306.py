# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-30 17:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrDisplay', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trclass',
            name='Prior_Int',
            field=models.IntegerField(default=0, verbose_name='Priority'),
        ),
    ]
