# Generated by Django 4.0.1 on 2022-02-02 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BLOG', '0009_alter_blogcomment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]