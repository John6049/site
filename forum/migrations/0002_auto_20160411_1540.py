# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date_updated',
        ),
        migrations.RemoveField(
            model_name='post',
            name='description',
        ),
        migrations.RemoveField(
            model_name='post',
            name='is_public',
        ),
        migrations.RemoveField(
            model_name='post',
            name='owner',
        ),
        migrations.AddField(
            model_name='post',
            name='number',
            field=models.IntegerField(default=0, verbose_name='number'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.TextField(verbose_name='title'),
        ),
    ]
