from django.contrib import admin
from django.urls import path

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_view),
    path('', home_view),
    path('students/', students_view, name='students'),
    path('students/<int:student_id>/', student_view),
    path('students/<int:student_id>/delete/', student_delete_view),
    path('authors/', authors_view, name='authors'),
    path('authors/<int:author_id>/delete/confirm/', author_delete_confirm_view),
    path('authors/<int:author_id>/delete/', author_delete_view),
    path('reader-students/', reader_students_view),
]
