from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Evento(models.Model):

    nome = models.CharField(_("Evento"), max_length=50)
    data = models.DateField(_("Data"), auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = _("Evento")
        verbose_name_plural = _("Eventos")

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("Evento_detail", kwargs={"pk": self.pk})

class Luta(models.Model):

    evento = models.ForeignKey("Evento", verbose_name=_("Evento"), on_delete=models.CASCADE, blank=True)
    lutadorA = models.ForeignKey("Lutador", verbose_name=_("Lutador 1"), on_delete=models.CASCADE, related_name='lutador', null=True, blank=True)
    lutadorB = models.ForeignKey("Lutador", verbose_name=_("Lutador 2"), on_delete=models.CASCADE, related_name='oponente', null=True, blank=True)
    card = models.ForeignKey("Card", verbose_name=_("Card"), on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = _("luta")
        verbose_name_plural = _("lutas")

    def __str__(self):
        return '{} x {}'.format(self.lutadorA, self.lutadorB)

    def get_absolute_url(self):
        return reverse("luta_detail", kwargs={"pk": self.pk})

class Lutador(models.Model):

    nome = models.CharField(_("Nome"), max_length=50)
    sobrenome = models.CharField(_("Sobrenome"), max_length=50)
    apelido = models.CharField(_("Apelido"), max_length=50, blank=True)
    

    class Meta:
        verbose_name = _("lutador")
        verbose_name_plural = _("lutadores")

    def __str__(self):
        return '{} {}'.format(self.nome, self.sobrenome)

    def get_absolute_url(self):
        return reverse("lutador_detail", kwargs={"pk": self.pk})

class Card(models.Model):

    tipos = (
        ('ME','Main Event'),
        ('CM','Co-Main Event'),
        ('CP','Card Principal'),
        ('CPM','Card Preliminar')
    )

    tipo = models.CharField(_("Card"), max_length=50, choices=tipos)
    
    class Meta:
        verbose_name = _("Card")
        verbose_name_plural = _("Cards")

    def __str__(self):
        return self.tipo

    def get_absolute_url(self):
        return reverse("card_detail", kwargs={"pk": self.pk})

class Resultado(models.Model):
    
    metodos = (
        ('UD','Decisão Unânime'),
        ('SD','Decisão Dividida'),
        ('MD','Decisão Majoritária'),
        ('KO','Nocaute'),
        ('TKO','Nocaute Técnico'),
        ('SUB','Finalização'),
        ('NC', 'No Contest'),
        ('EMP', 'Empate')
    )
    
    evento = models.ForeignKey("Evento", verbose_name=_("Evento"), on_delete=models.CASCADE)
    luta = models.ForeignKey("Luta", verbose_name=_("Luta"), on_delete=models.CASCADE)
    resultado = models.ForeignKey("Lutador", verbose_name=_("Resultado"), on_delete=models.CASCADE)
    metodo = models.CharField(_("Método"), max_length=50, choices=metodos)
    round = models.PositiveSmallIntegerField(_("Round"))
    
    class Meta:
        verbose_name = _("resultado")
        verbose_name_plural = _("resultados")

    def __str__(self):
        return '{} {} {}'.format(self.resultado, self.metodo, self.round)

    def get_absolute_url(self):
        return reverse("resultado_detail", kwargs={"pk": self.pk})
