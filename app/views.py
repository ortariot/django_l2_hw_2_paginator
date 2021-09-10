from django.core import paginator
from app.settings import BUS_STATION_CSV
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse(bus_stations, args=(1,)))


def bus_stations(request, page):

    path = BUS_STATION_CSV
    with open(path, encoding='cp1251') as file:
        reader = csv.DictReader(file)
        data = list(reader)
  
    print(page)
    
    paginate = Paginator(data, 10)

    data_list = paginate.get_page(page)
    next_page_url = f'/bus_stations?page={page + 1}'
    prev_page_url = f'/bus_stations?page={page - 1}'
    return render(request, 'index.html', context={
        'bus_stations': data_list,
        'current_page': page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })

