# Generated by Django 2.0.5 on 2018-09-05 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hele', '0010_nutri_of_food'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nutri_of_food',
            name='xuqinyu',
        ),
        migrations.AddField(
            model_name='nutri_of_food',
            name='fish',
            field=models.FloatField(null=True, verbose_name='鱼虾'),
        ),
        migrations.AddField(
            model_name='nutri_of_food',
            name='xuqin',
            field=models.FloatField(null=True, verbose_name='畜禽肉'),
        ),
    ]