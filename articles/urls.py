from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('board/', views.board, name="board"),
    path('board/<int:pk>', views.detail, name="detail"),
    path('create_page/', views.move_create, name="create_page"),
    path('create/', views.create, name="create"),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('update_page/<int:pk>', views.move_update, name="update_page"),
    path('update/<int:pk>', views.update, name="update"),
    path('<int:pk>/comments', views.comments_create, name='comments_create'),
]
