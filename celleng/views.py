from django.shortcuts import render
from celleng.models import Ceo, Group
from celleng.forms import FormCeo
# Create your views here.


def home(request):
    ceos = Ceo.objects.all()
    context = {
        "ceos" :  ceos,
    }
    return render(request,'index.html',context)

def form(request):
    form = FormCeo()
    
    context = {
        'form': form,
    }
    return render(request,'form.html',context)