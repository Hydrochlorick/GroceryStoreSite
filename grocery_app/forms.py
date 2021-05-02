from grocery_app.models import ItemCategory, GroceryStore
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.fields.core import FloatField
from wtforms.validators import DataRequired, Length, NumberRange, URL

class GroceryStoreForm(FlaskForm):
    title = StringField('Store Name', validators=[DataRequired(), Length(min=3, max=80)])
    address = StringField('Address', validators=[DataRequired(), Length(min=3)])
    submit = SubmitField('Submit')

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""
    name = StringField('Item Name', validators=[DataRequired(), Length(min=3, max=80)])
    price = FloatField('Price', validators=[DataRequired(), NumberRange(min=0.0)])
    category = SelectField('Category', validators=[DataRequired()], choices=ItemCategory.choices())
    photo_url = StringField('Photo URL')
    store = QuerySelectField('Store', query_factory=lambda: GroceryStore.query)
    submit = SubmitField('Submit')
    

