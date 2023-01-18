from django.urls import path
from . import views

app_name = "ideas"

urlpatterns= [
    path("", views.ideas_list, name="list"),
    path("ideas/create", views.ideas_create, name="create"),
    path("ideas/<int:pk>", views.ideas_read, name="read"),
    path("ideas/<int:pk>/update", views.ideas_update, name="update"),
    path("ideas/<int:pk>/delete", views.ideas_delete, name="delete"),
    
    path("devtool", views.devtools_list, name="devtool_list"),
    path("devtool/create", views.devtools_create, name="devtool_create"),
    path("devtool/<int:pk>", views.devtools_read, name="devtool_read"),
    path("devtool/<int:pk>/update", views.devtools_update, name="devtool_update"),
    path("devtool/<int:pk>/delete", views.devtools_delete, name="devtool_delete"),
]