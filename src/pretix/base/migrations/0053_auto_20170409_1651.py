# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-09 16:51
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


def migrate_global_settings(apps, schema_editor):
    GlobalSetting = apps.get_model('pretixbase', 'GlobalSetting')
    GlobalSettingsObject_SettingsStore = apps.get_model('pretixbase', 'GlobalSettingsObject_SettingsStore')

    l = []
    for s in GlobalSetting.objects.all():
        l.append(GlobalSettingsObject_SettingsStore(key=s.key, value=s.value))

    GlobalSettingsObject_SettingsStore.objects.bulk_create(l)


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0052_auto_20170324_1506'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EventSetting',
            new_name='Event_SettingsStore',
        ),
        migrations.RenameModel(
            old_name='OrganizerSetting',
            new_name='Organizer_SettingsStore',
        ),
        migrations.CreateModel(
            name='GlobalSettingsObject_SettingsStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, max_length=255)),
                ('value', models.TextField()),
            ],
        ),
        migrations.RunPython(
            migrate_global_settings, migrations.RunPython.noop
        ),
        migrations.DeleteModel(
            name='GlobalSetting',
        ),
        migrations.AlterField(
            model_name='event_settingsstore',
            name='object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='_settings_objects', to='pretixbase.Event'),
        ),
        migrations.AlterField(
            model_name='organizer_settingsstore',
            name='object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='_settings_objects', to='pretixbase.Organizer'),
        ),
    ]
