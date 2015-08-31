from django.contrib import admin
from agenda.Contato.models import Contato, agenda, carro, documentos, setor

class ContatoAdmin(admin.ModelAdmin):
	#model = Contato
	fields = ['contato_nome','contato_email','contato_sexo','contato_estado_civil','contato_telefone','contato_nascimento','contato_tipo_telefone','contato_cidade','contato_ativo']
	list_display = ['contato_nome', 'contato_email','contato_ativo', 'contato_nascimento']
	list_filter = ['contato_sexo', 'contato_estado_civil']
	search_fields = ['contato_nome']
	save_on_top = True
admin.site.register(Contato, ContatoAdmin)	


class agendaAdmin (admin.ModelAdmin):
	model = agenda
	list_display = ['agenda_assunto', 'agenda_dt_cadastro','agenda_dt_fim', 'agenda_finalizado']
	list_filter = ['agenda_assunto','agenda_dt_fim', 'agenda_finalizado']
	search_fields = ['agenda_assunto']
	save_on_top = True
admin.site.register(agenda, agendaAdmin)

class carroAdmin (admin.ModelAdmin):
	model = carro
	list_display = ['marca', 'modelo']
	list_filter = ['marca','modelo']
	search_fields = ['modelo']
	save_on_top = True
admin.site.register(carro, carroAdmin)

class documentosAdmin (admin.ModelAdmin):
	model = documentos
	list_display = ['rg', 'cpf']
	search_fields = ['cpf']
	save_on_top = True
admin.site.register(documentos, documentosAdmin)

class setorAdmin (admin.ModelAdmin):
	model = setor
	list_display = ['nome']
	search_fields = ['nome']
	save_on_top = True
admin.site.register(setor, setorAdmin)




# Register your models here.

