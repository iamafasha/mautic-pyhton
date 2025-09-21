from mautic import Client

def main():
       client = Client(
              base_url="http://localhost",
              client_key="key",
              client_secret="secret",
              call_back="http://localhost",
       )
       
       client.create_

main()