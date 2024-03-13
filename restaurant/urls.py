from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='new'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SinglMenuItemView.as_view()),
]
