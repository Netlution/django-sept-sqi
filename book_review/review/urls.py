from django.urls import path

from . import views

app_name = "review"

urlpatterns = [
    path("create-review/<int:book_id>/", views.create_review, name="create_review"),
    path("edit-review/<int:review_id>/", views.edit_review, name="edit_review"),
    path("confirm-delete-review/<int:review_id>/", views.confirm_delete_review, name="confirm_delete_review"),
    path("delete-review/<int:review_id>/", views.delete_review, name="delete_review"),
]