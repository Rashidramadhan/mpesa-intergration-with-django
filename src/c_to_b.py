import requests

from mpesa_intergration.src import keys
from mpesa_intergration.src.access_token import generate_token

my_access_token = generate_token()
def register_url():
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % my_access_token}
    request = {"ShortCode": keys.c2b_shortcode,
               "ResponseType": "Completed",
               "ConfirmationURL": "https://www.rashdjango.com/confirmation",
               "ValidationURL": "https://www.rashdjango.com/validation_url"
    }

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)

# register_url()


def simulate_transaction():
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    headers = {"Authorization": "Bearer %s" % my_access_token}
    request = {"ShortCode": keys.c2b_shortcode,
               "CommandID": "CustomerPayBillOnline",
               "Amount": "1",
               "Msisdn": keys.test_msisdn,
               "BillRefNumber": "1234565"}

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)

simulate_transaction()
