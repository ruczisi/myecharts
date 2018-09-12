# Generated by Django 2.0.5 on 2018-09-01 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hele', '0002_district_schools'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='geo_d',
            field=models.DecimalField(decimal_places=12, default=120, max_digits=15, verbose_name='维度'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='district',
            name='geo_l',
            field=models.DecimalField(decimal_places=12, default=40, max_digits=15, verbose_name='经度'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='district',
            name='schools',
            field=models.IntegerField(verbose_name='学校数'),
        ),
    ]
