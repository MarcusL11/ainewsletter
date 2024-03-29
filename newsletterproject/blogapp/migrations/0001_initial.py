# Generated by Django 5.0.3 on 2024-03-09 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TableOfContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, max_length=200, null=True)),
                ('order', models.IntegerField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Table of Contents',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(blank=True, max_length=100, null=True)),
                ('subtitle', models.TextField(blank=True)),
                ('content', models.TextField()),
                ('publish_date', models.DateField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('toc', models.ManyToManyField(blank=True, to='blogapp.tableofcontent')),
                ('tags', models.ManyToManyField(blank=True, to='blogapp.tag')),
            ],
        ),
    ]
