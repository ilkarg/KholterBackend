from django.urls import path
from modules.module_kholter import views

urlpatterns = [
    path('add/', views.ViewAddKholter.as_view()),
    path('get/', views.ViewGetKholter.as_view()),
    path('update/', views.ViewUpdateKholter.as_view()),
    path('delete/<id>', views.ViewDeleteKholter.as_view())
]
