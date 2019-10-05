class Account:
    #
    # Inital Thing
    #
    def __init__(self, client_id="", client_secret="", api_key=""):
        import requests
        from requests_oauthlib import OAuth2Session
        from oauthlib.oauth2 import BackendApplicationClient
        from oauthlib.oauth2 import TokenExpiredError

        # Self Things
        self.api_key = api_key
        self.client_id = client_id
        self.client_secret = client_secret

        # Gets The Token
        client = BackendApplicationClient(client_id=self.client_id)
        oauth = OAuth2Session(client=client)
        token = oauth.fetch_token(token_url="https://backpack.tf/oauth/access_token", client_id=self.client_id, client_secret=self.client_secret)
        
        self.token = token


    #
    # Gets a listing by id
    # 
    # id - the listing's ID
    #
    def getListing(self, listing_id=0):
        from requests_oauthlib import OAuth2Session
        from oauthlib.oauth2 import TokenExpiredError

        try:
            client = OAuth2Session(self.client_id, token=self.token)
            r = client.get("https://backpack.tf/api/1.0/classifieds/listings/" + str(listing_id))


        except TokenExpiredError as e:
            token = client.post("https://backpack.tf/oauth/access_token")
            self.token = token


        client = OAuth2Session(self.client_id, token=self.token)
        r = client.get("https://backpack.tf/api/1.0/classifieds/listings/" + str(listing_id))

    
    #
    # Delete a listing by ID
    # 
    # id - the listing's ID
    #
    def deleteListing(self, listing_id=0):
        from requests_oauthlib import OAuth2Session
        from oauthlib.oauth2 import TokenExpiredError

        try:
            client = OAuth2Session(self.client_id, token=self.token)
            r = client.delete("https://backpack.tf/api/1.0/classifieds/listings/" + str(listing_id))

        except TokenExpiredError as e:
            token = client.post("https://backpack.tf/oauth/access_token")
            self.token = token

        client = OAuth2Session(self.client_id, token=self.token)
        r = client.delete("https://backpack.tf/api/1.0/classifieds/listings/" + str(listing_id))


    #
    # Create a listing
    # 
    # intent - 0 (Buy) or 1 (Sell)
    # id - if intent is 1, the current id of the id you want to list
    # If buy order
    #    item_name - the item's name you want to buy
    #    quality - either the number or the text
    #    craftable - 0 or 1
    # offers - set to 0 for only accepting friend requests
    # buyout - set to 0 to allow negotiation
    # promoted - set to 1 to promote it, must be premium
    # details - the listing comment, max 200 characters
    # currencies - json of the currency EX: {"metal": 23}
    # PriceIndex - Most items is 0, however particle effects is the ID of the particle effect
    #   for crates it corresponds to the crate series, for strangifiers/unusualifiers is the
    #   definition index of the item it can be used on, chemistry set is a hyphented
    #   definition index 1086-14 is the index for a collector's festive wrangler
    #   here's a link to an item http://prntscr.com/pf2s0h
    #
    def createListing(self, intent=0, id=0, quality=6, item_name="Haunted Hat", craftable=1, priceindex=0, offers=0, buyout=1, promoted=0, details="", currencies={"metal": 0}, account_token=""):
        from requests_oauthlib import OAuth2Session
        from oauthlib.oauth2 import BackendApplicationClient
        from oauthlib.oauth2 import TokenExpiredError
        import urllib.parse
        import json
        import requests

        if intent == 0:
            payload = {
                "token": account_token,
                "listings": [
                    {
                        "intent": str(intent),
                        "item": {
                            "quality": str(quality),
                            "item_name": item_name,
                            "craftable": str(craftable),
                            "priceindex": str(priceindex)
                        },
                        "offers": str(offers),
                        "buyout": str(buyout),
                        "promoted": str(promoted),
                        "details": str(details),
                        "currencies": currencies
                    }
                ]
            }
        else:
            payload = {
                "token": account_token,
                "listings": [
                    {
                        "id": str(id),
                        "intent": str(intent),
                        "offers": str(offers),
                        "buyout": str(buyout),
                        "promoted": str(promoted),
                        "details": str(details),
                        "currencies": currencies
                    }
                ]
            }

        r = requests.post("https://backpack.tf/api/classifieds/list/v1", json=payload)
        print(r.text)