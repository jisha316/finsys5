# Generated by Django 4.0.4 on 2022-12-03 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0045_balance_sheet1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='balance_sheet1',
            name='bls',
        ),
        migrations.AddField(
            model_name='balance_sheet1',
            name='details1',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='balance_sheet1',
            name='details2',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
