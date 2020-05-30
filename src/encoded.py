import base64
from mpesa_intergration.src import keys


def generate_password(formated_date):
    data_to_encode = keys.business_shortcode + keys.lipa_na_mpesa_passkey + formated_date

    encoded_data = base64.b64encode(data_to_encode.encode())

    decoded_password = encoded_data.decode("utf-8")

    return decoded_password