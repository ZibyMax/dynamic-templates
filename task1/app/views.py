import csv
import os

#from app.settings import BASE_DIR
from django.conf import settings

from django.shortcuts import render
from django.views.generic import TemplateView

class InflationView(TemplateView):
    template_name = 'inflation.html'

    def get(self, request, *args, **kwargs):
        # чтение csv-файла и заполнение контекста
        context = {}
        DATA_CSV_FILE = os.path.join(settings.BASE_DIR, 'inflation_russia.csv')

        with open(DATA_CSV_FILE, 'r', encoding='UTF-8') as f:
            reader = csv.DictReader(f, delimiter=';')
            context['data'] = list(reader)

        context['headers'] = list(context['data'][0].keys())

        return render(request, self.template_name, context)
