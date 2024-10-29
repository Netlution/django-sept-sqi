from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from review.models import Book, Review

from .forms import ReviewForm

@login_required
def create_review(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Review added successfully")
            # return redirect(reverse("pages:book_detail", args=[book_id]))
            return redirect("pages:book_detail", book_id)
    context = {"form": form, "book": book}
    return render(request, "review/create-review.html", context)

@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    book = review.book
    form = ReviewForm(instance=review)
    if request.user != review.added_by:
        messages.error(request, "You do not have permission to edit that review")
        return redirect("pages:books") 
    if request.method == "POST":
        if not review.is_within_edit_window:
            messages.error(request, "You can only edit a review 5 minutes after posting it")
            return redirect(reverse("pages:book_detail", args=[book.id]))
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Review updated successfully")
            return redirect(reverse("pages:book_detail", args=[book.id]))
    context = {"form": form, "review": review, "book":book}
    return render(request, "review/edit-review.html", context)

@login_required
def confirm_delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    book = review.book
    if request.user != review.added_by:
        messages.error(request, "You do not have permission to edit that review")
        return redirect("pages:books") 
    context = {"review": review, "book":book}
    return render(request, "review/confirm-delete-review.html", context)

@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    book = review.book
    if request.user != review.added_by:
        messages.error(request, "You do not have permission to edit that review")
        return redirect("pages:books") 
    if request.method == "POST":
        review.delete()
        messages.success(request, "Review deleted successfully")
    return redirect(reverse("pages:book_detail", args=[book.id]))

    

    
