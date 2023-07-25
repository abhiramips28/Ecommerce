from django.urls import path
from django.views.generic import DetailView

from .views import ListCloths, AddToCartView, UpdateView
from . import views
urlpatterns = [
    path('cloths/',ListCloths.as_view(),name='cloths'),
    path('details/<int:pk>/', DetailView.as_view(), name='details'),
    path('update/<int:pk>/',UpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',DetailView.as_view,name='delete'),
    path('add-to-cart/', AddToCartView.as_view(), name='add-to-cart'),

]