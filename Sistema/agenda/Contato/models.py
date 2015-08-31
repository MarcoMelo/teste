from django.db import models

# Create your models here.
class Contato(models.Model):

	SEXO_CHOICES = (
		(u'masculino', u'Masculino'),
		(u'feminino', u'Feminino'),
		)
	ESTADO_CIVIL_CHOICES = (
		(u'solteiro', u'Solteiro'),
		(u'casado', u'Casado'),
		(u'divorciado', u'Divorciado'),
		(u'viuvo', u'Viuvo'),
		)

	TIPO_TELEFONE_CHOICES = (
		(u'fixo', u'Fixo'),
		(u'celular','Celular'),
		)

	contato_id = models.AutoField(primary_key=True)
	contato_nome = models.CharField(max_length=45)
	contato_nascimento = models.DateField()
	contato_sexo = models.CharField(max_length=50, choices=SEXO_CHOICES)
	contato_estado_civil = models.CharField(max_length=50, choices=ESTADO_CIVIL_CHOICES, verbose_name='Estado Civil')
	contato_email = models.CharField(max_length=50)
	contato_ativo = models.BooleanField(verbose_name='Ativo?')
	contato_telefone = models.CharField(max_length=12, null = True)
	contato_tipo_telefone = models.CharField(max_length=10, choices=TIPO_TELEFONE_CHOICES, verbose_name='Tipo Telefone' , null = True)
	contato_cidade = models.CharField(max_length=50 , null = True) 

	
class agenda(models.Model):
	agenda_id = models.AutoField(primary_key=True)
	agenda_assunto     = models.CharField(max_length=50)
	agenda_descricao   = models.TextField()
	agenda_dt_cadastro = models.DateField()
	agenda_dt_fim      = models.DateField()
	agenda_finalizado  = models.BooleanField(verbose_name='Finalizado?')
	
class carro(models.Model):
	marca = models.CharField(max_length=40)
	modelo = models.CharField(max_length=40)
	Contato= models.ForeignKey(Contato)

class documentos (models.Model):
	rg = models.CharField(max_length=15)
	cpf = models.CharField(max_length=11)
	Contato = models.OneToOneField(Contato)

class setor(models.Model):
	nome = models.CharField(max_length = 40)
	Contatos = models.ManyToManyField (Contato)

