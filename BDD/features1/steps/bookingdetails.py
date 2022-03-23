from behave import *
import requests

use_step_matcher("re")

tokens = []


@given('the (?P<name>.+) is signed in with (?P<email>.+) and (?P<password>.+) parameters')
def step_impl(context, name, email, password):
    url = f"http://127.0.0.1:5000/api/login"
    result = requests.request("POST", url, json=
        {
            "email": f"{email}",
            "name": f"{name}",
            "password": f"{password}"
        }
    )
    print("Username:", name, '\n', result.text)
    tokens.append(result.json()['access_token'])


@when("the user asks metrics from booking table")
def step_impl(context):

    url = f"http://127.0.0.1:5000/api/booking/2"
    for token in tokens :
        headers = {
            'Content-Type': "text/plain",
            'Connection': 'keep-alive',
            'Authorization': f"Bearer {token}"
        }
        response = requests.request("GET", url, headers=headers)

        context.response = response
        print(response.text)


@then('the user view details before confirmation with (?P<date>.+)')
def step_impl(context, date):
    status_code = context.response.status_code
    bookings = context.response.json()["booking_details"]
    assert status_code == 200
    assert bookings is not None

    for booking in bookings:
        if booking["booking_date"] >= date:
            print(booking)
    else:
        print("Booking's table doesn't find any records to show you")

