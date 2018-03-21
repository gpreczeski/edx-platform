# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entitlements', '0007_change_expiration_period_default'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseentitlementpolicy',
            name='mode',
            field=models.CharField(default=b'verified', max_length=32, choices=[(b'verified', b'verified'), (b'professional', b'professional')]),
        ),
    ]
