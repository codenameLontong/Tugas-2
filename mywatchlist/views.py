from django.shortcuts import render
from mywatchlist.models import Movies
from django.http import HttpResponse
from django.core import serializers

# Failed Bonus
def status(request):
    list = Movies.objects.all()
    counter = 0
    for watchlist in list:
        if watchlist.watched == "True":
            counter += 1
    if counter >= len(list) - counter:
        return "Selamat, kamu sudah banyak menonton!"
    else:
        return "Wah, kamu masih sedikit menonton!"

# Show watchlist function for header
def show_watchlist(request):
    data_watchlist = Movies.objects.all()
    context = {
        'list' : data_watchlist,
        'nama': 'Jeremy Mervin',
        'id' : '2106654675',
    }
    return render(request, "mywatchlist.html", context)

# XML function
def show_xml(request):
    data = Movies.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# JSON function
def show_json(request):
    data = Movies.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = Movies.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_xml_by_id(request, id):
    data = Movies.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_item_by_id(request):
    data_watchlist = Movies.objects.filter(pk=id)
    context = {
        'list': data_watchlist,
        'nama': 'Jeremy Mervin',
        'id' : '2106654675',
    }
    return render(request, "mywatchlist.html", context)