# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=128)),
                ('value', models.IntegerField(verbose_name='Point Value')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=128)),
                ('slug', models.SlugField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='challenge',
            name='competition',
            field=models.ForeignKey(to='competitions.Competition', related_name='challenges'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='challenge',
            name='solver',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True, related_name='solved_challenges'),
            preserve_default=True,
        ),
    ]
