# Generated by Django 2.2.5 on 2020-01-27 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billetera', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimiento',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='billetera.Categoria'),
        ),
    ]