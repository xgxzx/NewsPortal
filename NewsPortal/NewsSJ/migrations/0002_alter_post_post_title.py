# Generated by Django 4.1.4 on 2023-01-19 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsSJ', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_title',
            field=models.CharField(max_length=256, verbose_name='Post name'),
        ),
    ]
