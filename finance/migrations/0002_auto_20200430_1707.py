# Generated by Django 2.2.12 on 2020-04-30 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finance',
            name='executor_role',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='finance',
            name='function',
            field=models.IntegerField(default=1),
        ),
    ]
