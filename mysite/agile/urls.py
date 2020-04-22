from .views import PrincipleList, ValuesList

from django.urls import path

urlpatterns = [
    path('principles', PrincipleList.as_view(), name='principle-list'),
    path('values', ValuesList.as_view(), name='values-list'),
]