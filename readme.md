# Using nested resources: Beer Ratings

Today, we are going to be creating an app that allows users to review their favorite beers. Just about everyone likes beer, and life is too short to drink Keystone Light and/or Milwaukee's Best.

In our app, we're going to use `devise` to take care of our user authentication. A user can sign up, find a list of beers, and leave a review for a beer. A beer can have many reviews and when all the beers are listed, you can click on an individual beer and see all the relevant reviews. When you sign in, you can see all the reviews you've left on different beers

For the purposes of our basic CRUD app today, anyone can create a beer. A beer does not need to have a `user_id`

Release 1: Generate Models/Migrations
------------------

Release 2: Authentication using `devise`
------------------
Simple log in and log out functionality only

Release 3: CRUD Beers/Reviews (Nested)
------------------------------
