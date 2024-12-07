from django.shortcuts import render, redirect
from .forms import DataForm
from . models import Data

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dash-pred')
    else:
        form = DataForm()
    context = {
        'form':form,
    }
    return render(request, 'dash/index.html', context)

def pred(request):
    predicted_sports = Data.objects.all()
    context = {
        'predicted_sports': predicted_sports
    }
    return render(request, 'dash/pred.html',context)