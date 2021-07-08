from django import http
from django.shortcuts import redirect, render
from .forms import BeerForm
from django.http import HttpResponse
from .models import Beer, Review


# Helper methods
def get_beer(beer_id):
    return Beer.objects.get(id=beer_id)


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
    return render(request, 'ratings/home.html')
