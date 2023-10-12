from django.urls import path, re_path
import menu.views as menu

urlpatterns = [
    path('', menu.index, name='index'),
    re_path(r'^(\d+)', menu.index, name='index')
]