# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tribute', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('position', models.IntegerField()),
                ('card_type', models.IntegerField(choices=[(0, 'Period'), (1, 'Event'), (2, 'Scene'), (3, 'Legacy')])),
                ('title', models.CharField(max_length=200)),
                ('is_bright', models.BooleanField()),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_edit', models.DateTimeField(blank=True, null=True)),
                ('big_picture', models.CharField(max_length=500)),
                ('palette', models.TextField(max_length=200, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='card',
            name='game_id',
            field=models.ForeignKey(to='tribute.Game'),
        ),
        migrations.AddField(
            model_name='card',
            name='parent',
            field=models.ForeignKey(to='tribute.Card'),
        ),
    ]
