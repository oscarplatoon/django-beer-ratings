from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from beer_ratings_app.models import Beer, Review
from beer_ratings_app.forms import BeerForm, ReviewForm

def index(request):
    info = {
        "all_beers": Beer.objects.all() # SELECT * FROM beer_ratings_app_beer;
    }
    return render(request, "pages/beer/beer_list.html", info)


def beer_detail(request, beer_id):
    try:
        beer = Beer.objects.get(id=beer_id)
    except:
        return HttpResponse(f"A beer with id {beer_id} doesn't exist!")

    info = {
        "beer": beer
    }
    return render(request, "pages/beer/beer_detail.html", info)


def review_list(request, beer_id):
    try:
        beer = Beer.objects.get(id=beer_id)
    except:
        return HttpResponse(f"A beer with id {beer_id} doesn't exist!")

    info = {
        "beer": beer
    }
    return render(request, "pages/review/review_list.html", info)

def review_detail(request, beer_id, review_id):
    try:
        review = Review.objects.get(id=review_id)
    except:
        return HttpResponse(f"A review with id {review_id} doesn't exist!")

    info = {
        "review": review
    }
    return render(request, "pages/review/review_detail.html", info)


def review_new(request, beer_id):
    try:
        beer = Beer.objects.get(id=beer_id)
    except:
        return HttpResponse(f"A beer with id {beer_id} doesn't exist!")
    
    form = ReviewForm(request.POST or None, initial={"beer": beer})

    return process_review_form(request, "Add", form, beer)


def review_update(request, beer_id, review_id):
    try:
        review = Review.objects.get(id=review_id)
    except:
        return HttpResponse(f"A review with id {review_id} doesn't exist!")

    form = ReviewForm(request.POST or None, instance=review)

    return process_review_form(request, "Update", form, review.beer)
    

def process_review_form(request, action, form, beer):

    review = None
    if request.method == "POST":
        try:
            review = form.save()
            return redirect("review_detail", beer_id=review.beer.id, review_id=review.id)
        except:
            return HttpResponse("You failed!")

    info = {
        "action": action,
        "beer": beer,
        "form": form
    }
    return render(request, "pages/review/review_form.html", info)


def review_delete(request, beer_id, review_id):
    try:
        review = Review.objects.get(id=review_id)
        review.delete()
    except:
        return HttpResponse(f"A review with id {review_id} doesn't exist!")

    return redirect("review_list", beer_id=beer_id)