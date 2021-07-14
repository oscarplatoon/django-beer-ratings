from django.shortcuts import render, redirect
from .models import Beer, Review
from .forms import BeerForm, ReviewForm

def get_beer(beer_id):
    return Beer.objects.get(id=beer_id)

def beer_list(request):
    beers = Beer.objects.all()
    return render(request, 'beers/beers_list.html', {'beers': beers})

def beer_detail(request, beer_id):
    beer = get_beer(beer_id)
    return render(request, 'beers/beer_detail.html', {'beer': beer})

def new_beer(request):
    if request.method == "POST":
        form = BeerForm(request.POST)
        if form.is_valid():
            beer = form.save(commit=False)
            beer.save()
            return redirect('beer_detail', beer_id=beer.id)
    else:
        form = BeerForm()
    return render(request, 'beers/beer_form.html', {'form': form, 'type_of_request': 'New'})

def edit_beer(request, beer_id):
    beer = get_beer(beer_id)
    if request.method == "POST":
        form = BeerForm(request.POST, instance=beer)
        if form.is_valid():
            beer = form.save(commit=False)
            beer.save()
            return redirect('beer_detail', beer_id=beer.id)
    else:
        form = BeerForm(instance=beer)
    return render(request, 'beers/beer_form.html', {'form': form, 'type_of_request': 'Edit'})

def delete_beer(request, beer_id):
    if request.method == "POST":
        beer = get_beer(beer_id)
        beer.delete()
    return redirect('beers_list')


def get_review(review_id):
    return Review.objects.get(id=review_id)

def review_list(request, beer_id):
    beer = get_beer(beer_id)
    reviews = beer.reviews.all()
    return render(request, 'reviews/review_list.html', {'beer': beer, 'reviews': reviews})

def review_detail(request, beer_id, review_id):
    beer = get_beer(beer_id)
    review = get_review(review_id)
    return render(request, 'reviews/review_detail.html', {'beer': beer, 'review': review})

def new_review(request, beer_id):
    beer = get_beer(beer_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.beer = beer
            review.save()
            return redirect('review_detail', beer_id=review.beer.id, review_id=review.id)
    else:
        form = ReviewForm()
    return render(request, 'reviews/review_form.html', {'form': form, 'type_of_request': 'New'})

def edit_review(request, beer_id, review_id):
    beer = get_beer(beer_id)
    review = get_review(review_id)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            return redirect('review_detail', review_id=review.id, beer_id=beer_id)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'reviews/review_form.html', {'form': form, 'type_of_request': 'Edit'})
