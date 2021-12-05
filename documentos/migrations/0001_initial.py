# Generated by Django 3.2.9 on 2021-12-04 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('data_pesquisa', models.DateField()),
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('data_nascimento', models.DateField()),
                ('cep', models.CharField(max_length=8)),
                ('cpf', models.CharField(max_length=11)),
                ('celular', models.CharField(max_length=11)),
            ],
        ),
    ]