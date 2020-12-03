from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import QabulForm, AloqaForm
from .models import *


def index(request):
    qabul_form = QabulForm()
    if request.method == 'POST':
        name = request.POST.get('name', None)
        service = request.POST.get('service', None)
        master = request.POST.get('master', None)
        phone = request.POST.get('phone', None)
        date = request.POST.get('date', None)
        message = request.POST.get('message', None)
        qabul_form = QabulForm(request.POST)
        messages.success(request, "Xurmatli sayt adminstratori sizga yangi xabar keldi.")
        if qabul_form.is_valid():
            qabul_form.save()
            # Qabul.objects.create()
        print(request)

    return render(request, 'uno.html', {'form': qabul_form})



def bizhaqimizda(request):
    return render(request, 'about.html')



def aloqa(request):
    if request.method == 'POST':
        form = AloqaForm(request.POST)
        if form.is_valid():
            data = Aloqa_New()#create relation with model
            data.name=form.cleaned_data['name']#get form input data
            data.phone = form.cleaned_data['phone']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']

            data.save()#save data to table
            messages.success(request, "Xurmatli sayt adminstratori sizga yangi xabar keldi.")
            return HttpResponseRedirect('/aloqa/')


    form = AloqaForm

    context = {
         'form': form,
    }
    return render(request, 'contact.html', context)
