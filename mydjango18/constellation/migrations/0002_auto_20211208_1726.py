# Generated by Django 3.2.9 on 2021-12-08 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constellation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='day',
        ),
        migrations.RemoveField(
            model_name='post',
            name='month',
        ),
        migrations.AddField(
            model_name='post',
            name='end_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='post',
            name='start_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
    ]