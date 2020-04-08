# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2020-04-07 17:52
from __future__ import unicode_literals

from django.db import migrations, models
import helpers.director.model_func.cus_fields.cus_picture
import helpers.director.model_func.cus_fields.jsonable


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200, verbose_name='菜名称')),
                ('cover', helpers.director.model_func.cus_fields.cus_picture.PictureField(max_length=300, verbose_name='封面')),
                ('used_resource', helpers.director.model_func.cus_fields.jsonable.JsonAbleField(default=[], verbose_name='消耗原料')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200, verbose_name='原料名称')),
                ('amount', models.FloatField(default=0, verbose_name='剩余总量')),
            ],
        ),
    ]
