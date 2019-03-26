import csv
import os

from app.settings import BASE_DIR

from django.shortcuts import render
from django.views.generic import TemplateView

class InflationView(TemplateView):
    template_name = 'inflation.html'

    def get(self, request, *args, **kwargs):
        # чтение csv-файла и заполнение контекста
        context = {}
        DATA_CSV_FILE = os.path.join(BASE_DIR, 'inflation_russia.csv')
        context['data'] = []

        with open(DATA_CSV_FILE, 'r', encoding='UTF-8') as f:
            reader = csv.DictReader(f, delimiter=';')
            for line in reader:
                context['data'].append(line)

        context['headers'] = [
            'Год',
            'Январь',
            'Февраль',
            'Март',
            'Апрель',
            'Май',
            'Июнь',
            'Июль',
            'Август',
            'Сентябрь',
            'Октябрь',
            'Ноябрь',
            'Декабрь',
            'Всего'
        ]

        return render(request, self.template_name, context)
