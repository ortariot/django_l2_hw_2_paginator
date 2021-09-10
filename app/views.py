from app.settings import STATION_LIST
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    page = int(request.GET.get('page', 1))
    paginate = Paginator(STATION_LIST, 10)
    data_list = paginate.get_page(page)
    next_page_url = f'/bus_stations?page={page + 1}'\
                    if data_list.has_next() else None
    prev_page_url = f'/bus_stations?page={page - 1}'\
                    if data_list.has_previous() else None
    return render(request, 'index.html', context={
        'bus_stations': data_list,
        'current_page': page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })
