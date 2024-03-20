from django.shortcuts import redirect, render
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm

    if request.method =='POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid(): # Devuelve True si todos los campos estan correctos. 
            # ⇊ Se recupera la informacion del formulario ⇊
            name = request.POST.get('name','') 
            email = request.POST.get('email','')
            content = request.POST.get('content','')

            # ⇊ Envio de correo y redireccion ⇊
            email = EmailMessage(
                'La Caffettiera: Nuevo mensaje de contacto', # Asunto
                'De {} <{}>\n\nEscribió:\n\n{}'.format(name, email, content), # Cuerpo
                'no-contestar@inbox.mailtrap.io', # email_origen
                ['pantunez@leafnoise.io'], # email_destino,
                reply_to=[email]
            )
            try:
                email.send()
                # reverse: permite hacer una redireccion pasandole un path permitiendo este ser escalable. 
                return redirect(reverse('contact')+'?ok') # Redirecciona a la misma url pero con una variable 'ok' 
            except:
                return redirect(reverse('contact')+'?fail')
    return render(request, 'contact/contact.html', {'form':contact_form})