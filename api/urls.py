from django.urls import path

from .views import SpendingList

urlpatterns = [
    path("spendings/", SpendingList.as_view()),
]
