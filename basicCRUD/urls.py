from django.urls import path
from.import views

urlpatterns = [
    path('', views.index, name='index'),
    path('students/<int:student_id>', views.show, name='show'),
    path('students/<int:student_id>/delete', views.delete, name='delete'),
    path('students/add', views.store, name="store"),
    path('students/<int:student_id>/update', views.update, name="update")
]