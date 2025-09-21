import requests
from .contact import Contact

class Client(object):
    """
    A client for Mautic API
    """

    def __init__(self, 
                 version,
                 base_url, 
                 client_key, 
                 client_secret, 
                 call_back
       ):
        
        self.base_url = base_url
        self.client_key = client_key
        self.client_secret = client_secret
        self.call_back = call_back
        self.version = version

    @property
    def contact(self):
        return Contact()