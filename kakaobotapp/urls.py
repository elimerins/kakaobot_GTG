from django.urls import path,include

from .import views

urlpatterns=[
    path('keyboard/',views.keyboard),
    path('',views.index),
    path('message',views.answer)
]
