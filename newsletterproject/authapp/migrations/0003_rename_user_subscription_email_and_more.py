# Generated by Django 5.0.3 on 2024-03-10 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_subscription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='user',
            new_name='email',
        ),
        migrations.AlterField(
            model_name='subscription',
            name='tier',
            field=models.CharField(default='Free', max_length=100),
        ),
    ]
