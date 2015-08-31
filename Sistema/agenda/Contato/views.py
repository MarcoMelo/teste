from django.shortcuts import render

def home(request):
	return render(request, 'index.html')
def avaliar(request):
	return render(request, 'avaliar.html')
def apresentacao(request):
	return render(request, 'apresentacao.html')
# Create your views here.
