# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0002_auto_20141107_1838'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hint',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('text', models.CharField(max_length=2048)),
                ('challenge', models.ForeignKey(to='competitions.Challenge', related_name='hints')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='challenge',
            name='description',
            field=models.CharField(default='', max_length=2048, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='challenge',
            name='url',
            field=models.URLField(default='', blank=True),
            preserve_default=False,
        ),
    ]
