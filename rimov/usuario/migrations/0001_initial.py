# Generated by Django 3.1.6 on 2021-02-05 14:44

import django.contrib.auth.models
from django.db import migrations, models
import rimov.usuario.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('tipo', models.CharField(choices=[('ADMINISTRADOR', 'Administrador'), ('CORRETOR', 'Corretor')], default='CORRETOR', help_text='* Campos obrigatórios', max_length=15, verbose_name='Tipo do usuário *')),
                ('avatar', models.ImageField(default='media/media/avatar.jpg', upload_to='media/')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome completo *')),
                ('numero_cri', models.CharField(blank=True, max_length=100, null=True, verbose_name='Registro CRI *')),
                ('telefone', models.CharField(blank=True, max_length=100, null=True, verbose_name='Telefone')),
                ('instagram', models.CharField(max_length=100, null=True, verbose_name='Perfil Instagram *')),
                ('facebook', models.CharField(max_length=100, null=True, verbose_name='Perfil Facebook *')),
                ('email', models.EmailField(db_index=True, max_length=100, unique=True, verbose_name='Email')),
                ('is_active', models.BooleanField(default=False, help_text='Se ativo, o usuário tem permissão para acessar o sistema', verbose_name='Ativo')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, verbose_name='Hash')),
            ],
            options={
                'verbose_name': 'usuário',
                'verbose_name_plural': 'usuários',
                'ordering': ['nome'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
                ('administradores', rimov.usuario.models.AdministradorAtivoManager()),
                ('corretores', rimov.usuario.models.CorretorAtivoManager()),
            ],
        ),
    ]
