# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('post_create_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Blog_Post',
                'verbose_name_plural': 'Blog_Posts',
                'ordering': ['-post_create_date'],
            },
        ),
    ]
