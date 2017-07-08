# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-08 06:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0003_auto_20170708_1417'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryTemp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(verbose_name='章节id')),
                ('group', models.IntegerField(verbose_name='所属课程id')),
                ('name', models.CharField(max_length=100, verbose_name='章节名称')),
            ],
            options={
                'db_table': 'category_temp',
                'verbose_name': '章节',
                'verbose_name_plural': '章节',
            },
        ),
    ]