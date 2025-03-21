# Generated by Django 5.1.7 on 2025-03-13 15:50

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('content', models.TextField()),
                ('excerpt', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('minutes_to_read', models.PositiveIntegerField(default=5)),
                ('tags', models.ManyToManyField(related_name='blog_posts', to='blog.tag')),
            ],
            options={
                'ordering': ['-date_posted'],
            },
        ),
    ]
