# Generated by Django 2.1.2 on 2018-11-17 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsessex', '0002_auto_20181117_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='contact',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
