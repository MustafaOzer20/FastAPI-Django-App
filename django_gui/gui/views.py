from django.shortcuts import render
from django.http import HttpResponse
from gui.forms import DriverFilterForm
import requests
import datetime

def index(request):
    return HttpResponse("<h1>Hello World!</h1>")


def get_drivers(request):
    fastapi_url = "http://127.0.0.1:8001/fetch_drivers"

    if request.method == "POST":
        form = DriverFilterForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['startDate']
            end_date = form.cleaned_data['endDate']
            min_score = form.cleaned_data['minScore']
            max_score = form.cleaned_data['maxScore']
            limit = form.cleaned_data['limit']
            offset = form.cleaned_data['offset']

    else:
        form = DriverFilterForm()
        this_year = datetime.datetime.now().year
        start_date = f"{this_year - 20}-01-01"
        end_date = f"{this_year}-01-01"
        min_score = 0
        max_score = 10
        limit = 50
        offset = 0

    response = requests.get(fastapi_url, params={
            'startDate': start_date,
            'endDate': end_date,
            'minScore': min_score,
            'maxScore': max_score,
            'limit': limit,
            'offset': offset
        })

    response_data = response.json()
    context = {'data': response_data, 'form': form}
    return render(request, 'drivers.html', context)

