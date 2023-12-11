# app/search/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class SearchForm(FlaskForm):
    """
    Form for users to enter search queries without additional metadata.
    """
    # Define a search field which requires some data to be submitted and also restrict the length of the search query
    search_query = StringField('Search', validators=[
                               DataRequired(), Length(min=2, max=200)])

    # Submit button to send the form data to the server
    submit = SubmitField('Search')
