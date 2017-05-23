# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import RegModelForm,ContactForm
from .models import Registrados

# Create your views here.


def inicio(request):
	titulo="Ola ke ase"
	if request.user.is_authenticated():
		titulo="Bienvenido amo del calabozo %s" %(request.user)
	form=RegModelForm(request.POST or None)

	context={
				"titulo":titulo,
				"el_form":form,
			}


	if form.is_valid():
		instance=form.save(commit=False)
		if not instance.nombre:
			instance.nombre="Anonimous"
		instance.save()

		context={
			"titulo":"Gracias %s!!!" %(instance.nombre),
		}

		if not instance.nombre:
			context={
				"titulo":"Gracias %s!!!" %(instance.email),
			}


		print instance
		#form_data = form.cleaned_data
		#abc = form_data.get("email")
		#abc2 = form_data.get("nombre")
		#obj = Registrados.objects.create(email=abc,nombre=abc2)

	return render(request,"inicio.html",context)

def contact(request):
	form=ContactForm(request.POST or None)
	if form.is_valid():
		#for key,value in form.cleaned_data.iteritems():
			#print key,value
		#for key in form.cleaned_data:
			#print key
			#print form.cleaned_data.get(key)
		#print email,mensaje,nombre
		form_email=form.cleaned_data.get("email")
		form_mensaje=form.cleaned_data.get("mensaje")
		form_nombre=form.cleaned_data.get("nombre")
		asunto='Form de Contacto'
		email_from=settings.EMAIL_HOST_USER
		email_to=[email_from,"otroemail@gmail.com"]
		email_mensaje="%s:%s enviado por %s" %(form_nombre,form_mensaje,form_email)
		send_mail(asunto,
			email_mensaje,
			email_from,
			email_to,
			fail_silently=True
			)

	context={
		"form":form,
	}
	return render(request,"forms.html",context)