import json
import base64
import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth


class Credentials:
    consumer_key = "z9XxgDsSA0iQxqHv1j0D7bcv4UrejgFj"
    consumer_secret = "PlEgGEFvUp5M8GrF"
    passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
    api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

class MpesaAccessToken:
    token = requests.get(Credentials.api_url, auth=HTTPBasicAuth(Credentials.consumer_key, Credentials.consumer_secret))
    access_token = json.loads(token.text)
    validated_token = access_token['access_token']

class MpesaPassword:
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    shortcode = "174379"
    offSetValue = "0"
    passkey = Credentials.passkey

    encodes = shortcode + passkey + timestamp

    encoded = base64.b64encode(encodes.encode())

    decoded_password = encoded.decode('utf-8')
    
    # data_to_encode = Credentials.shortcode + Credentials.passkey + MpesaAccessToken.validated_token
    # encoded = base64.b64encode(data_to_encode.encode())
    # decoded_password = encoded.decode('utf-8')
    # password = {"password": decoded_password}


