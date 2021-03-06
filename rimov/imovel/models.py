from django.db import models
from django.urls import reverse_lazy
from rimov.usuario.models import Funcionario


STATUS = (
    ("D", "Disponível"),
    ("I", "Indisponível")

)
TIPO_PROPRIEDADE = (
    ("Apartamento", "Apartamento"),
    ("Casa", "Casa"),
    ("Casa Condomínio", "Casa Condomínio"),
    ("Casa Vila", "Casa Vila"),
    ("Cobertura", "Cobertura"),
    ("Comercial", "Comercial"),
    ("Fazenda", "Fazenda"),
    ("Flat", "Flat"),
    ("Kitnet", "Kitnet"),
    ("Loft", "Loft"),
    ("Sobrado", "Sobrado"),
    ("Terreno", "Terreno Padrão"),

)

CATEGORIA = (
    ("Alto Padrão", "Alto Padrão"),
    ("Médio Padrão", "Médio Padrão"),
    ("Baixo Padrão", "Baixo Padrão")

)

NEGOCIO = (
    ("Aluguel", "Aluguel"),
    ("Arrendamento", "Arrendamento"),
    ("Em Construção", "Em Construção"),
    ("Venda", "Venda")

)


class Imovel(models.Model):
    titulo = models.CharField(max_length=250)
    propriedade = models.TextField(choices=TIPO_PROPRIEDADE, blank=True, null=True)
    negocio = models.TextField(choices=NEGOCIO, blank=True, null=True)
    categoria = models.TextField(choices=CATEGORIA, blank=True, null=True)
    valor = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    localizacao = models.CharField(max_length=300, blank=True, null=True)
    endereco = models.CharField(max_length=300, blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)
    num_quarto = models.IntegerField(blank=True, null=True)
    num_banheiro = models.IntegerField(blank=True, null=True)
    num_vaga = models.IntegerField(blank=True, null=True)
    descricao = models.TextField(unique=True, blank=True, null=True)
    corretor = models.ForeignKey(Funcionario, on_delete=models.CASCADE, blank=True, null=True)
    status = models.TextField(choices=STATUS)
    video = models.CharField(max_length=3000, blank=True, null=True)

    def imagens_url(self):
        if self.imagens and hasattr(self.imagens, 'url'):
            return self.imagens.url

    class Meta:
        ordering = ['-pk']
        verbose_name = "imóvel"
        verbose_name_plural = "imóveis"

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse_lazy('imovel:imovel_detail', kwargs={'id': self.id})

    def first_image(self):
        if self.imagem_imoveis:
            return self.imagem_imoveis.first()


class Galeria(models.Model):
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE, related_name='imagem_imoveis', null=True)
    imagem = models.FileField('Imagem', upload_to='media', blank=False, null=True)

    class Meta:
        verbose_name = "Galeria do Imóvel"
        verbose_name_plural = "Galeria do Imóvel"
