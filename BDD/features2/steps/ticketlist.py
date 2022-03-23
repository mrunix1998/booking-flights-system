from behave import *
import requests

# use_step_matcher("re")
use_step_matcher("parse")

tokens = []


@given("the {name} is signed in with {email} and {password} parameters")
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


@when("the user asks {flight_id} metrics from flights table")
def step_impl(context, flight_id):
    url = f"http://127.0.0.1:5000/api/flight"
    for token in tokens:
        headers = {
            'Content-Type': "text/plain",
            'Connection': 'keep-alive',
            'Authorization': f"Bearer {token}"
        }
        response = requests.request("GET", url, headers=headers)

        context.response = response
        status_code = context.response.status_code
        flights = context.response.json()["flights"]
        assert status_code == 200
        assert flights is not None

        for flight in flights:
            if flight["flight_id"] == int(flight_id):
                print(flight)
        else:
            print("Flight's table doesn't find any records to show you")


@then("the user sees the desired flights with {src_city} and {dst_city} and {date}")
def step_impl(context, src_city, dst_city, date):

    status_code = context.response.status_code
    flights = context.response.json()["flights"]
    assert status_code == 200
    assert flights is not None

    for flight in flights:
        if flight["arrival_city"] == src_city or flight["departure_city"] == dst_city or flight["departure_date"] <= date:
            print(flight)
    else:
        print("Flight's table doesn't find any records to show you")