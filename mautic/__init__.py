import requests
from mautic.__init__ import Client

class Client(object):
    """
    A client for Mautic API
    """

    def __init__(self, base_url, client_key, client_secret, call_back):
        self.base_url = base_url
        self.client_key = client_key
        self.client_secret = client_secret
        self.call_back = call_back

__all__ = ['Client']