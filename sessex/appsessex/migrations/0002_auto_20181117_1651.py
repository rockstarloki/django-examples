# Generated by Django 2.1.2 on 2018-11-17 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsessex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='contact',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
