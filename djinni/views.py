from django.shortcuts import render
from django.views import generic

from djinni.models import VacancyDjinni


class VacancyListView(generic.ListView):
    model = VacancyDjinni
    template_name = "djinni/vacancies.html"
    context_object_name = "vacancies_list"
