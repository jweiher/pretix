# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 11:26
from __future__ import unicode_literals

from django.db import migrations, models


def assign_positions(app, schema_editor):
    Invoice = app.get_model('pretixbase', 'Invoice')

    for i in Invoice.objects.iterator():
        for j, l in enumerate(i.lines.all()):
            l.position = j
            l.save()


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0075_orderfee'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoiceline',
            name='position',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='orderfee',
            name='fee_type',
            field=models.CharField(choices=[('payment', 'Payment fee'), ('shipping', 'Shipping fee'), ('other', 'Other fees')], max_length=100),
        ),
        migrations.RunPython(
            assign_positions, migrations.RunPython.noop
        ),
        migrations.AlterModelOptions(
            name='invoiceline',
            options={'ordering': ('position', 'pk')},
        ),
    ]
