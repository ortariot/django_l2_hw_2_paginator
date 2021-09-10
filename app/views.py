from app.settings import BUS_STATION_CSV
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    path = BUS_STATION_CSV
    with open(path, encoding='cp1251') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    current_page = 1
    next_page_url = 'write your url'
    return render(request, 'index.html', context={
        'bus_stations': data,
        'current_page': current_page,
        'prev_page_url': None,
        'next_page_url': next_page_url,
    })

