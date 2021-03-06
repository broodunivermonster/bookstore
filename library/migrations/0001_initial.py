# Generated by Django 2.2.12 on 2020-04-30 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cate_id', models.PositiveSmallIntegerField(primary_key=True, serialize=False, verbose_name='category id')),
                ('name', models.CharField(max_length=256, unique=True)),
            ],
            options={
                'ordering': ['cate_id'],
            },
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('ISBN', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(default='anonymous', max_length=100)),
                ('publisher', models.CharField(default='anonymous', max_length=100)),
                ('publish_date', models.DateField()),
                ('advertise', models.CharField(max_length=1000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('inventory', models.IntegerField(default=0)),
                ('cover', models.FileField(upload_to='static/common/book_cover')),
                ('cate_id', models.ForeignKey(default={'cate_id': 0}, on_delete=django.db.models.deletion.CASCADE, to='library.Category')),
            ],
        ),
    ]
