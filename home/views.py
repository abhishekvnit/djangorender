from django.shortcuts import render
from home.models import TalcherDirect


# Create your views here.

def index(request):

    db= TalcherDirect.objects.all()

    
    return render(request,'home.html',{'db': db})