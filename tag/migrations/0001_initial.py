# Generated by Django 3.1.1 on 2020-09-17 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='태그명')),
                ('registered_dttm', models.DateTimeField(auto_now_add=True, verbose_name='작성시간')),
            ],
            options={
                'verbose_name': '김민혁 커뮤니티 태그',
                'verbose_name_plural': '김민혁 커뮤니티 태그',
                'db_table': 'campus_tag',
            },
        ),
    ]
