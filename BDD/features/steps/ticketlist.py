from behave import *
import requests

use_step_matcher("re")

tokens = []

@when("the user asks metrics from flights")
def step_impl(context):
    pass
    # raise NotImplementedError(u'STEP: When  the user asks metrics from flights')


@then("the user sees the desired flights with (?P<date>.+)")
def step_impl(context, date):
    pass


