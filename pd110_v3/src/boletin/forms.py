from django import forms

from .models import Registrados

class RegModelForm(forms.ModelForm):
	class Meta:
		model = Registrados
		fields = ["nombre","email"]

	def clean_email(self):
		email = self.cleaned_data.get("email")
		email_base,proveeder=email.split("@")
		dominio,extension=proveeder.split(".")
		if not extension=="edu":
			raise forms.ValidationError("Utilizar extension .EDU")
		return email

	def clean_nombre(self):
		nombre=self.cleaned_data.get("nombre")
		return nombre

class RegForm(forms.Form):
	nombre=forms.CharField(max_length=100)
	email=forms.EmailField()