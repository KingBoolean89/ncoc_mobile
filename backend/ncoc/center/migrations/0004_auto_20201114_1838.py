# Generated by Django 3.1.3 on 2020-11-14 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0003_auto_20201114_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='center',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='dailyreport',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
