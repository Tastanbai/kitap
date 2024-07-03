from django.urls import path, re_path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('login/', views.user_login, name='login'),  
    path('', views.index, name='index'),
    path('excel/', views.excel, name='excel'),
    path('excel_user/', views.excel_user, name='excel_user'),
    path('send-email/', views.send_email, name='send_email'),
    path('rent_book/', views.rent_book, name='rent_book'),
    path('blacklist/', views.blacklist, name='blacklist'),
    path('view_returned_books/', views.view_returned_books, name='view_returned_books'),
    path('logout/', views.logout, name='logout'),
    path('tastanbek28012002/', views.reg, name='reg'),
    path('add_book/', views.add_book, name='add_book'),
    path('add_publish/', views.add_publish, name='add_publish'),
    path('rent_book/return/<int:publish_id>/book', views.return_book, name='return_book'),
    path('edit/<int:id>/book/', views.edit_book, name='edit_book'),
    path('delete_books/', views.delete_books, name='delete_books'),
    path('select_all_books/', views.select_all_books, name='select_all_books'),
]