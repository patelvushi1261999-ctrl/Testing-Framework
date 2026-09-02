from behave import given, when, then, parsers
import re

# -----------------------------
# Zomato restaurant search
# -----------------------------
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

# -----------------------------
# Flipkart product search
# -----------------------------
@given("I launch the browser")
def launch_browser(context):
    print("Launching browser...")

@given("I navigate to the Flipkart homepage")
def navigate_flipkart(context):
    print("Navigating to Flipkart homepage...")

@when('I enter "{search_term}" in the search box')
def enter_search_term(context, search_term):
    context.search_term = search_term
    print(f"Entering search term: {search_term}")

@then("I should see laptop products listed")
def verify_laptops(context):
    print("Laptop products displayed.")

@then("I should see shoe products listed")
def verify_shoes(context):
    print("Shoe products displayed.")

@then("I should see mobile products listed")
def verify_mobiles(context):
    print("Mobile products displayed.")

# -----------------------------
# BookMyShow movie booking
# -----------------------------
@given("I open the BookMyShow app")
def open_bookmyshow(context):
    print("Opening BookMyShow app...")

@given("I log in with valid credentials")
def login_bookmyshow(context):
    print("Logging in with valid credentials...")

@when('I choose seat type "{seat_type}"')
def choose_seat(context, seat_type):
    context.seat_type = seat_type
    print(f"Selected seat type: {seat_type}")

@when('I pay using "{payment_method}"')
def pay_method(context, payment_method):
    context.payment_method = payment_method
    print(f"Payment method: {payment_method}")

@then('I should see booking confirmation for "{seat_type}" with "{payment_method}"')
def booking_confirmation(context, seat_type, payment_method):
    print(f"Booking confirmed for {seat_type} seat with {payment_method} payment.")
