from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home),
    path('addapi',views.addapi),
    path('delete',views.delete),
    path('update',views.update)
]
