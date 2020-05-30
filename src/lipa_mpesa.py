import requests
from mpesa_intergration.src import keys

from mpesa_intergration.src.access_token import generate_token
from mpesa_intergration.src.encoded import generate_password
from mpesa_intergration.src.utilities import get_format_date



def lipa_na_mpesa():
    formated_date = get_format_date()
    decoded_password = generate_password(formated_date)
    access_token = generate_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": keys.business_shortcode,
        "Password": decoded_password,
        "Timestamp": formated_date,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "5",
        "PartyA": keys.phone_number,
        "PartyB": keys.business_shortcode,
        "PhoneNumber": keys.phone_number,
        "CallBackURL": "https://www.rashdjango.com/lipanampesa",
        "AccountReference": "123567",
        "TransactionDesc": "test fee"
    }

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)

lipa_na_mpesa()