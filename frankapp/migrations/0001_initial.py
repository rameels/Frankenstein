# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ActorsRoles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actor', models.ForeignKey(to='frankapp.Actors')),
            ],
        ),
        migrations.CreateModel(
            name='Crew',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CrewResponsibilities',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('crew', models.ForeignKey(to='frankapp.Crew')),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('duration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EventsTimes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('daytime', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(to='frankapp.Events')),
            ],
        ),
        migrations.CreateModel(
            name='Responsibilities',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Stages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='events',
            name='stage',
            field=models.ForeignKey(to='frankapp.Stages'),
        ),
        migrations.AddField(
            model_name='crewresponsibilities',
            name='responsibility',
            field=models.ForeignKey(to='frankapp.Responsibilities'),
        ),
        migrations.AddField(
            model_name='crewresponsibilities',
            name='stage',
            field=models.ForeignKey(to='frankapp.Stages'),
        ),
        migrations.AddField(
            model_name='actorsroles',
            name='eventstimes',
            field=models.ForeignKey(default=1, to='frankapp.EventsTimes'),
        ),
        migrations.AddField(
            model_name='actorsroles',
            name='role',
            field=models.ForeignKey(to='frankapp.Roles'),
        ),
    ]
