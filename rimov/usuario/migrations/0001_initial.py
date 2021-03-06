# Generated by Django 3.1.6 on 2021-02-06 20:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('ADMINISTRADOR', 'Administrador'), ('CORRETOR', 'Corretor')], default='CORRETOR', help_text='Campos obrigatórios', max_length=15, verbose_name='tipo do usuário')),
                ('avatar', models.ImageField(default='media/media/avatar.jpg', upload_to='media/')),
                ('cri', models.CharField(blank=True, max_length=100, null=True, verbose_name='registro CRI')),
                ('telefone', models.CharField(blank=True, max_length=100, null=True, verbose_name='telefone')),
                ('instagram', models.CharField(blank=True, max_length=400, null=True, verbose_name='perfil Instagram')),
                ('facebook', models.CharField(blank=True, max_length=400, null=True, verbose_name='perfil Facebook')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='usuário')),
            ],
            options={
                'verbose_name': 'funcionário',
                'verbose_name_plural': 'funcionários',
                'ordering': ('usuario__first_name',),
            },
        ),
    ]
