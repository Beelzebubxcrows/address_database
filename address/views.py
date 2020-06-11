from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from address.models import address
# Create your views here.

class addaddress(CreateView):
    model = address
    fields = '__all__'


def success(request):
    return render(request,'success.html')



def show(request):
    addresses = address.objects.all()
    
    return render(request, 'showaddress.html', {'address':addresses})

    
    
def base(request):

    return render(request,'landing.html')
