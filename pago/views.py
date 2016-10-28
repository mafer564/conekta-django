from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .models import Sale
from django.core import serializers

class Pago(View):
    def get(self, request):
        template_name = 'pago.html'
        return render(request, template_name)

    def post(self, request):
        print('gfsdgfgfgggsgddg')
        print(request.POST["conektaTokenId"])
        token_id = request.POST["conektaTokenId"]
        sale = Sale()
        if token_id: #Prevents send empty token
            return HttpResponse(sale.charge(300, token_id))

class Histo(View):
    def get(self, request):
        nombres=name.objects.all()
        tarjetas=number.objets.all()
        data=serializers.serialize('json',posts,numbers)
        return HttpResponse(data,content_type='aplication/json')