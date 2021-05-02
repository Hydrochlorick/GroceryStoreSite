from grocery_app.forms import GroceryItemForm, GroceryStoreForm
from flask import Blueprint, request, render_template, redirect, url_for, flash
from datetime import date, datetime
from grocery_app.models import GroceryStore, GroceryItem
# from forms import GroceryStoreForm, GroceryItemForm
# from grocery_app.forms import BookForm, AuthorForm, GenreForm

# Import app and db from events_app package so that we can run app
from grocery_app import app, db

main = Blueprint("main", __name__)

##########################################
#           Routes                       #
##########################################

@main.route('/')
def homepage():
    all_stores = GroceryStore.query.all()
    print(all_stores)
    return render_template('home.html', all_stores=all_stores)

@main.route('/new_store', methods=['GET', 'POST'])
def new_store():
    form = GroceryStoreForm()

    # If form was submitted and was valid:
    if form.validate_on_submit():
        # Create a new GroceryStore object and save it to the database
        new_store = GroceryStore(
            title = form.title.data,
            address = form.address.data
        )
        db.session.add(new_store)
        db.session.commit()

        # Flash a success message
        flash("Hey it might've worked.")
        # Redirect the user to the store detail page.
        return redirect(url_for('main.store_detail', store_id=new_store.id))

    # Send the form to the template and use it to render the form fields
    return render_template('new_store.html', form=form)

@main.route('/new_item', methods=['GET', 'POST'])
def new_item():
    form = GroceryItemForm()

    # If form was submitted and was valid:
    if form.validate_on_submit():
        # Create a new GroceryItem object and save it to the database
        new_item = GroceryItem(
            name = form.name.data,
            price = form.price.data,
            category = form.category.data,
            photo_url = form.photo_url.data,
            store = form.store.data,
            store_id = form.store.data.id
        )
        db.session.add(new_item)
        db.session.commit()

        # Flash a success message
        flash("Hey this probably worked.")
        # Redirect the user to the item detail page.
        return redirect(url_for('main.item_detail', item_id = new_item.id))
    print(form.errors)
    # Send the form to the template and use it to render the form fields
    return render_template('new_item.html', form=form)

@main.route('/store/<store_id>', methods=['GET', 'POST'])
def store_detail(store_id):
    store = GroceryStore.query.get(store_id)
    # Create a GroceryStoreForm and pass in `obj=store`
    form = GroceryStoreForm(obj=store)

    # If form was submitted and was valid:
    if form.validate_on_submit():
        # Create a new GroceryStore object and save it to the database
        new_store = GroceryStore(
            title = form.title.data,
            address = form.address.data
        )
        db.session.add(new_store)
        db.session.commit()

        # Flash a success message
        flash("Hey it might've worked.")
        # Redirect the user to the store detail page.
        return redirect(url_for('main.store_detail', store=new_store))

    # Send the form to the template and use it to render the form fields
    return render_template('store_detail.html', store=store, form=form)

@main.route('/item/<item_id>', methods=['GET', 'POST'])
def item_detail(item_id):
    item = GroceryItem.query.get(item_id)
    print(item_id)
    print(item)
    # Create a GroceryItemForm and pass in `obj=item`
    form = GroceryItemForm(obj=item)

    # If form was submitted and was valid:
    if form.validate_on_submit():
        # Create a new GroceryItem object and save it to the database
        # new_item = GroceryItem(
        #     name = form.name.data,
        #     price = form.price.data,
        #     category = form.category.data,
        #     photo_url = form.photo_url.data,
        #     store = form.store.data,
        #     store_id = form.store.data.id
        # )
        item.name = form.name.data
        item.price = form.price.data,
        item.category = form.category.data,
        item.photo_url = form.photo_url.data,

        db.session.add(new_item)
        db.session.commit()

        # Flash a success message
        flash("Hey this probably worked.")
        # Redirect the user to the item detail page.
        return redirect(url_for('main.item_detail', item_id = item.id))

    # Send the form to the template and use it to render the form fields
    return render_template('item_detail.html', item=item, form=form)

