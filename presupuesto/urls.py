from django.contrib import admin
from django.urls import path
from billetera import views

urlpatterns = [
    path('', views.getBadget, name="home"),
    path('movimiento/', views.Movement, name="movimiento"),
    path('admin/', admin.site.urls),
]
