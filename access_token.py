import requests
from requests.auth import HTTPBasicAuth
from mpesa_intergration import keys


def generate_token():
    consumer_key = keys.consumer_key
    consumer_secret = keys.consumer_secret
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"


    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    json_response = r.json()
    # print(r.json()) == {'access_token': '1HAtPOWx8rc8OnVNIgJ2S4WF3x5d', 'expires_in': '3599'}

    my_access_token = json_response['access_token']

    return my_access_token