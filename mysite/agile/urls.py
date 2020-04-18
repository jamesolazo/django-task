from .views import PrincipleListView, ValuesListView

from django.urls import path

urlpatterns = [
    path('principles', PrincipleListView.as_view(), name='principle-list'),
    path('values', ValuesListView.as_view(), name='values-list'),
]