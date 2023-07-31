from django.shortcuts import render,HttpResponse 

def hello_world(request,nome,idade):
    return HttpResponse(f"<h1><p><strong>Hello {nome} de {idade}</strong></p></h1>")
