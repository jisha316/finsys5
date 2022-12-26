# Generated by Django 4.0.4 on 2022-12-03 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0040_alter_profit_loss_details2'),
    ]

    operations = [
        migrations.CreateModel(
            name='balancesheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(max_length=255, null=True)),
                ('account', models.CharField(max_length=255, null=True)),
                ('transactions', models.CharField(max_length=255, null=True)),
                ('accname', models.CharField(max_length=255, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('details0', models.CharField(max_length=255, null=True)),
                ('details1', models.CharField(blank=True, max_length=255, null=True)),
                ('details2', models.CharField(blank=True, default='', max_length=255)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('payments', models.IntegerField(blank=True, null=True)),
                ('bill', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.purchasebill')),
                ('cid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
                ('debit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.purchasedebit')),
                ('expnc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.purchase_expense')),
                ('invc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.invoice')),
                ('pymnt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.purchasepayment')),
            ],
        ),
    ]