# Generated by Django 2.0.5 on 2018-09-01 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hele', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='schools',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]