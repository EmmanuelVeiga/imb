# Generated by Django 3.1.6 on 2021-02-22 02:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0004_auto_20210213_2047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('propriedade', models.TextField(blank=True, choices=[('Apartamento', 'Apartamento'), ('Casa', 'Casa'), ('Casa Condomínio', 'Casa Condomínio'), ('Casa Vila', 'Casa Vila'), ('Cobertura', 'Cobertura'), ('Comercial', 'Comercial'), ('Fazenda', 'Fazenda'), ('Flat', 'Flat'), ('Kitnet', 'Kitnet'), ('Loft', 'Loft'), ('Sobrado', 'Sobrado'), ('Terreno', 'Terreno Padrão')], null=True)),
                ('negocio', models.TextField(blank=True, choices=[('Aluguel', 'Aluguel'), ('Arrendamento', 'Arrendamento'), ('Em Construção', 'Em Construção'), ('Venda', 'Venda')], null=True)),
                ('categoria', models.TextField(blank=True, choices=[('Alto Padrão', 'Alto Padrão'), ('Médio Padrão', 'Médio Padrão'), ('Baixo Padrão', 'Baixo Padrão')], null=True)),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('localizacao', models.CharField(blank=True, max_length=300, null=True)),
                ('endereco', models.CharField(blank=True, max_length=300, null=True)),
                ('area', models.IntegerField(blank=True, null=True)),
                ('num_quarto', models.IntegerField(blank=True, null=True)),
                ('num_banheiro', models.IntegerField(blank=True, null=True)),
                ('num_vaga', models.IntegerField(blank=True, null=True)),
                ('descricao', models.TextField(blank=True, null=True, unique=True)),
                ('status', models.TextField(choices=[('D', 'Disponível'), ('I', 'Indisponível')])),
                ('video', models.CharField(blank=True, max_length=3000, null=True)),
                ('corretor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.funcionario')),
            ],
            options={
                'verbose_name': 'imóvel',
                'verbose_name_plural': 'imóveis',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.FileField(null=True, upload_to='media', verbose_name='Imagem')),
                ('imovel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='imagem_imoveis', to='imovel.imovel')),
            ],
            options={
                'verbose_name': 'Galeria do Imóvel',
                'verbose_name_plural': 'Galeria do Imóvel',
            },
        ),
    ]
