from django.shortcuts import render
from django.http import HttpResponse
from .forms import MedicineForm

# Create your views here.

def index(request):

    # Page from the theme 
    return render(request, 'pages/index.html')

def purchasing(request):
  return render(request, 'pages/purchasing.html', { 'segment': 'purchasing' })

def medicine(request):
  return render(request, 'pages/medicine.html', { 'segment': 'medicine' })

def sell(request):
  return render(request, 'pages/sell.html', { 'segment': 'sell' })

def distributor(request):
  return render(request, 'pages/distributor.html', { 'segment': 'distributor' })


def create_product(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = MedicineForm()
    return render(request, 'create_product.html', {'form': form})
