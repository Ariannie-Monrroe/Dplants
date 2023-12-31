# Generated by Django 4.2.2 on 2023-06-23 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dplants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoriaId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dplants.categoria'),
        ),
        migrations.AlterField(
            model_name='vendido',
            name='categoriaId_vendido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dplants.categoria'),
        ),
    ]
