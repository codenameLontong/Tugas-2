from django.shortcuts import render
from katalog.models import CatalogItem

# Create your views here.
def show_katalog(request):
    data_catalog = CatalogItem.objects.all()
    context = {
        'list_barang': data_catalog,
        'nama': 'Mervin',
        'id' : '2106654675'
    }
    return render(request, "katalog.html", context)