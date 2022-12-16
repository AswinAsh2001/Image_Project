from .import views
from django.urls import path

urlpatterns = [
    path('',views.base,name='base'),
    path('add_emp',views.add_emp,name='add_emp'),
    path('show_emp',views.show_emp,name='show_emp'),
    path('editpage/<int:pk>',views.editpage,name='editpage'),
    path('edit_emp/<int:pk>',views.edit_emp,name='edit_emp'),
]