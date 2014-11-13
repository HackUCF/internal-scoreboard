# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0003_auto_20141110_0515'),
    ]

    operations = [
        migrations.RenameField(
            model_name='challenge',
            old_name='solver',
            new_name='solvers',
        ),
    ]
