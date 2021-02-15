# Generated by Django 3.1.6 on 2021-02-13 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_auto_20210213_2047'),
        ('imovel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imovel',
            name='corretor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.funcionario'),
        ),
        migrations.AlterField(
            model_name='imovel',
            name='status',
            field=models.TextField(choices=[('D', 'Disponível'), ('I', 'Indisponível')]),
        ),
    ]