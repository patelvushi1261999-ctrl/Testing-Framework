from behave import given, when, then
from behave import step
from behave import use_fixture
from behave import fixture
from behave import parsers
import re

# 1. Zomato-style restaurant search
@given("I open the Zomato app")
def open_zomato(context):
    print("Opening Zomato app...")

@when('I search for cuisine "{cuisine}"')
def search_cuisine(context, cuisine):
    context.cuisine = cuisine
    print(f"Searching for cuisine: {cuisine}")

@then("I should see matching restaurant names")
def verify_restaurants(context):
    print(f"Restaurants displayed for cuisine: {context.cuisine}")

# 2. Movie rating with parse step parser
@when(parsers.parse('I rate the movie "{movie}" as {rating:d} stars'))
def rate_movie(context, movie, rating):
    print(f"Movie: {movie}, Rating: {rating} stars")

# 3. Flipkart-style product filter with regex parser
@when(re.compile(r'I filter category "(?P<category>.+)" with price range "(?P<price_range>.+)"'))
def filter_products(context, category, price_range):
    print(f"Filtering category: {category}, Price range: {price_range}")

# 4. BookMyShow ticket booking with fixture to share state
@fixture
def movie_fixture(context, movie_name):
    context.selected_movie = movie_name
    yield context.selected_movie

@given('I select the movie "{movie_name}"')
def select_movie(context, movie_name):
    use_fixture(movie_fixture, context, movie_name)
    print(f"Selected movie: {movie_name}")

@then("I should see booking confirmation")
def booking_confirmation(context):
    print(f"Booking confirmed for movie: {context.selected_movie}")

# 5. WhatsApp-like message sending feature
@when(parsers.parse('I send a message "{message}" to contact "{contact}"'))
def send_message(context, message, contact):
    print(f"Sending message: '{message}' to contact: {contact}")
