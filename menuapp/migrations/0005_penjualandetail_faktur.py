# Generated by Django 4.2.4 on 2023-10-29 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menuapp', '0004_profitsummary'),
    ]

    operations = [
        migrations.AddField(
            model_name='penjualandetail',
            name='faktur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menuapp.penjualanfaktur'),
        ),
    ]
