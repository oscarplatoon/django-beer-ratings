# Using Nested Resources: Beer Ratings

Today, we are going to be creating an app that allows users to review their favorite beers. Just about everyone likes beer, and life is too short to drink Keystone Light and/or Milwaukee's Best.

In our app, a user can sign up, find a list of beers, and leave a review for a beer. A beer can have many reviews and when all the beers are listed, you can click on an individual beer and see all the relevant reviews. When you sign in, you can see all the reviews you've left on different beers.

For the purposes of our basic CRUD app today, anyone can create a beer.

Release 0: Users Logging In/Out
----------------
Create a new Django App, with postgresql as a database, and user authentication. Tutorials are your friend when you start programming. [This](https://wsvincent.com/django-user-authentication-tutorial-login-and-logout/) is a great one. So is [this](https://github.com/oscarplatoon/curriculum/blob/master/week-06/2021-06-28.md) one ;)

Once you've `pip install`ed everything you need in your virtual environment, you can `pip freeze > requirements.txt`. That 'freezes' all the requirements of your virtual environment so that you can install everything at once later on with `pip install -r requirements.txt`

Release 1: Generate Models/Migrations
-------------------------------------
In `beer-rating/ratings/models.py`, create models for `Beer` and `Review`. A Beer can have many reviews and a review belongs to a beer. Then, create a few beers to use as test data. 

Release 2: CRUD Beers/Reviews (Nested)
--------------------------------------
Now add your routes so that users can add, update, and delete reviews for a beer. Users should be able to see all reviews for a beer, but should only be able to update and delete reviews that they created. 

Stretch: Search box, Seed with faker
--------------------------------------
Create a search box that lets users search for matching beers and/or reviews. To test this functionality, use [faker](https://github.com/joke2k/faker/) to seed your database with lots of entries! Faker has lots of [options](https://faker.readthedocs.io/en/master/locales/en_US.html).
