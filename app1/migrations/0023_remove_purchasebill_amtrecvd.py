# Generated by Django 4.0.4 on 2022-11-08 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0022_purchaseorder_amtrecvd_purchaseorder_balance_due'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchasebill',
            name='amtrecvd',
        ),
    ]