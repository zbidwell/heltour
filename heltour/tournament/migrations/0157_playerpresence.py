# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-30 00:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0156_modrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerPresence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('first_msg_time', models.DateTimeField(blank=True, null=True)),
                ('last_msg_time', models.DateTimeField(blank=True, null=True)),
                ('online_for_game', models.BooleanField(default=False)),
                ('pairing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.PlayerPairing')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.Player')),
                ('round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.Round')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]