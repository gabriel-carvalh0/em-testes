from django import forms
from django.core.mail import send_mail
from django.conf import settings

class ContactForm(forms.Form):
	name = forms.CharField(label='Nome')
	email = forms.EmailField(label="E-mail")
	message = forms.CharField(label="Menssagem", widget=forms.Textarea)


	def send_mail(self):
		name = self.cleaned_data['nome']
		email = self.cleaned_data['E-mail']
		message = self.cleaned_data['Menssagem']
		message = 'Name : {0}/nE-Mail:{1}/n{2}'.format(name, email, message)
		send_mail(
			'Contato da Brioch commerce',message, settings.DEFAULT_FROM_EMAIL,
			[settings.DEFAULT_FROM_EMAIL]
			)

