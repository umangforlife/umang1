# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-17 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20180716_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='ngo',
            field=models.CharField(choices=[('SP', 'Sarasprayas'), ('V', 'Vikas'), ('PA', 'PAWS'), ('PF', 'PoshFoundation'), ('LN', 'LakshyamNGODelhi'), ('CW', 'ChildWomenCareSociety'), ('SA', 'Shivashrya'), ('SK', 'Satkartar')], max_length=2, null=True),
        ),
    ]
