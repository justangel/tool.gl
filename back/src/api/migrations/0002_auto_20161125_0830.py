# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 08:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scenerevision',
            name='child',
        ),
        migrations.AlterField(
            model_name='metascene',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='Array of tag-names', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='scenerevision',
            name='parent',
            field=models.ForeignKey(blank=True, help_text='Reference to parent Revision', null=True, on_delete=django.db.models.deletion.CASCADE, to='api.SceneRevision'),
        ),
        migrations.AlterField(
            model_name='scenerevision',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='Array of tag-names', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
