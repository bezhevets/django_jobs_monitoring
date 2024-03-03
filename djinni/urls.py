from django.urls import path

from djinni.views import VacancyListView

urlpatterns = [
    path("", VacancyListView.as_view(), name="vacancies-list"),
]

app_name = "djinni"
