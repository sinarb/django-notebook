from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home_config, name='main'),
    path('detail/<int:user_id>', views.detail, name='detail'),
    path('add/', views.add, name='add_note'),
    path('edit/<int:user_id>', views.edit, name='edit_note'),
    path('search/', views.search, name='search'),
    path('delete/<int:user_id>', views.delete, name='delete')
]