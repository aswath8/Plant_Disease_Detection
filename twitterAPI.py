# Search for the latest tweets about #pycon
from twitter import *

API_key= "runsra61MhrLsjwgOYlANBzu9"
API_secret_key= "fVChsb8y4Aq9zGqgYrINmza8klJobvkWhZdkXhZxhjxGGa4OMZ"
Bearer_token="AAAAAAAAAAAAAAAAAAAAAKnhNAEAAAAArNhv2G5CX0S8z8BAnNQVojvgOtk%3DfYUxJgFxW4e6LAmoXtm2vhpvv7rIP3AUIO7rGJOaPXz70fRCPM"

access_token="1364862750518730752-h0V0VfPBpc8pB97dmsHqTS0bGErn1o"
access_secret_token="q9Pj0olBCb9vbI1DOYe2jP26VWB8Xvy8RfFqbQtAFMifN"


token=access_token
token_secret=access_secret_token
consumer_key=API_key
consumer_secret=API_secret_key


t = Twitter(
    auth=OAuth(token, token_secret, consumer_key, consumer_secret))

s=t.search.tweets(q="#pycon")
