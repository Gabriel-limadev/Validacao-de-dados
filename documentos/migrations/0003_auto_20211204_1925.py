# Generated by Django 3.2.9 on 2021-12-04 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0002_auto_20211204_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='celular',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='registro',
            name='cpf',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='registro',
            name='rg',
            field=models.CharField(max_length=9),
        ),
    ]