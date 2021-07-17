from django import http
from django.shortcuts import redirect, render
from .forms import BeerForm, ReviewForm
from django.http import HttpResponse
from .models import Beer, Review


# Helper methods
def get_beer(beer_id):
    return Beer.objects.get(id=beer_id)


def get_review(review_id):
    return Review.objects.get(id=review_id)


# Views
def create_beer(request):
    if request.method == 'POST':
        filled_out_beer_form = BeerForm(request.POST)
        new_beer = filled_out_beer_form.save()
        return redirect('ratings:show_beer', beer_id=new_beer.id)
    else:
        beer_form = BeerForm()
        context = {'form': beer_form, 'type_of_form': 'New'}
        return render(request, 'ratings/beer_form.html', context)


def show_beer(request, beer_id):
    beer = get_beer(beer_id)
    context = {'beer': beer}
    return render(request, 'ratings/beer.html', context)


def show_beers(request):
    beers = Beer.objects.all()
    context = {'beers': beers}
    return render(request, 'ratings/beers_list.html', context)


def edit_beer(request, beer_id):
    beer = get_beer(beer_id)

    if request.method == 'POST':
        filled_out_beer_form = BeerForm(request.POST, instance=beer)
        new_beer = filled_out_beer_form.save()
        return redirect('ratings:show_beer', beer_id=new_beer.id)
    else:
        beer_form = BeerForm(instance=beer)
        context = {'form': beer_form, 'type_of_form': 'Edit'}
        return render(request, 'ratings/beer_form.html', context)


def delete_beer(request, beer_id):
    beer = get_beer(beer_id)
    beer.delete()
    return redirect('ratings:show_beers')


def home(request):
    reviews = Review.objects.filter(author=request.user)
    context = {'reviews': reviews}
    return render(request, 'ratings/home.html', context)

# Review views


def create_review(request, beer_id):
    beer = get_beer(beer_id)

    if request.user.is_authenticated:
        if request.method == 'POST':
            filled_out_review_form = ReviewForm(request.POST)
            new_review = filled_out_review_form.save(commit=False)
            new_review.beer = beer
            new_review.author = request.user
            new_review.save()
            return redirect('ratings:show_reviews', beer_id=beer_id)
        else:
            review_form = ReviewForm()
            context = {'form': review_form,
                       'type_of_form': 'New', 'beer': beer}
            return render(request, 'ratings/review_form.html', context)

    return redirect('ratings:home')


def show_reviews(request, beer_id):
    beer = get_beer(beer_id)
    reviews = Review.objects.filter(beer=beer)
    context = {'beer': beer, 'reviews': reviews}
    return render(request, 'ratings/beer_reviews.html', context)


def show_review(request, beer_id, review_id):
    beer = get_beer(beer_id)
    review = get_review(review_id)

    context = {'beer': beer, 'review': review}

    return render(request, 'ratings/review.html', context)


def edit_review(request, beer_id, review_id):
    beer = get_beer(beer_id)
    review = get_review(review_id)

    if request.method == 'POST':
        filled_out_review_form = ReviewForm(request.POST, instance=review)
        new_review = filled_out_review_form.save()
        new_review.save()
        return redirect('ratings:show_review', beer_id=beer_id, review_id=review_id)
    else:
        review_form = ReviewForm(instance=review)
        context = {'form': review_form,
                   'type_of_form': 'Edit', 'beer': beer}
        return render(request, 'ratings/review_form.html', context)


def delete_review(request, beer_id, review_id):
    review = get_review(review_id)
    review.delete()
    return redirect('ratings:show_reviews', beer_id=beer_id)
