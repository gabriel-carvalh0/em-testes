from django import forms
from django.core.mail import send_mail
from django.conf import settings

class ContactForm(forms.Form):
	name = forms.CharField(label='Nome')
	email = forms.EmailField(label="E-mail")
	message = forms.CharField(label="Menssagem", widget=forms.Textarea())


	# def send_mail(send_mail):
	# 	name = self.cleaned_data.get('name')
	# 	email = self.cleaned_data.get('email')
	# 	message = self.cleaned_data.get('message')
	# 	message = 'Name : {0}\nE-Mail:{1}\n"{2}"'.format(name, email, message)

	# 	if len(name) < 4:
	# 		raise forms.ValidationError('escolha um nome com mais de 4 letras')
	# 	return name

	# 	send_mail(
	# 		'Contato da Brioch commerce',message, settings.EMAIL_HOST_USER,
	# 		[settings.EMAIL_HOST_USER]
	# 		)

