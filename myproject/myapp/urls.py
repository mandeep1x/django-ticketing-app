from django.urls import path
from .import views

urlpatterns = [
    path('events/', views.events_list),
    path('items/', views.items_list),
    # path()
]

    
