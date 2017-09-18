# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-14 12:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0004_auto_20170914_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='archives.Location'),
        ),
        migrations.AlterField(
            model_name='person',
            name='other_names',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='archives.Title'),
        ),
        migrations.AlterField(
            model_name='work',
            name='shape',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='archives.Shape'),
        ),
        migrations.AlterField(
            model_name='work',
            name='subject_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='archives.Location'),
        ),
        migrations.AlterField(
            model_name='work',
            name='support',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='archives.Support'),
        ),
    ]