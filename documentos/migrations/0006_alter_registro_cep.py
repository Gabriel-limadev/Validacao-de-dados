# Generated by Django 3.2.9 on 2021-12-04 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0005_remove_registro_rg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='cep',
            field=models.CharField(max_length=9),
        ),
    ]
