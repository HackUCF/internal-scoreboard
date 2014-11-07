# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChallengeCategory',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=32, unique=True, help_text='Put it in lowercase, for style.')),
            ],
            options={
                'verbose_name_plural': 'Challenge categories',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='challenge',
            name='category',
            field=models.ForeignKey(to='competitions.ChallengeCategory', null=True, blank=True, related_name='challenge'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='competition',
            name='internal',
            field=models.BooleanField(verbose_name='Scored internally', default=False),
            preserve_default=True,
        ),
    ]
