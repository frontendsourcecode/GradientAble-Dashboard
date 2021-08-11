from django.urls import path
from . import views

app_name = "dashboard"


urlpatterns = [
    path('', views.index, name="dashboard"),
    path('alert/', views.alert, name="alert"),
    path('button/', views.button, name="button"),
    path('badge/', views.badge, name="badge"),
    path('pagination/', views.pagination, name="pagination"),
    path('card/', views.card, name="card"),
    path('collapse/', views.collapse, name="collapse"),
    path('carousel/', views.carousel, name="carousel"),
    path('progress/', views.progress, name="progress"),
    path('grid/', views.grid, name="grid"),
    path('modal/', views.modal, name="modal"),
    path('spinner/', views.spinner, name="spinner"),
    path('tabs/', views.tabs, name="tabs"),
    path('typography/', views.typography, name="typography"),
    path('tooltip/', views.tooltip, name="tooltip"),
    path('toast/', views.tooltip, name="toast"),
    path('form/', views.form, name="form"),
    path('table/', views.form, name="table"),
    path('chart/', views.chart, name="chart"),
    path('chart/', views.chart, name="chart"),
    path('map/', views.map, name="map"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
]
