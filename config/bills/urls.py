from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add-expense/", views.add_expense, name="add_expense"),
    path("add-member/", views.add_member, name="add_member"),
    path("edit-expense/<int:id>/", views.edit_expense, name="edit_expense"),
    path("delete-expense/<int:id>/", views.delete_expense, name="delete_expense"),
]