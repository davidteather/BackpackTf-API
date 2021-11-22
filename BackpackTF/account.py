from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import TokenExpiredError
from oauthlib.oauth2 import BackendApplicationClient
import requests
import urllib.parse
import json
import requests
from lxml import html


class Account:
    #
    # Inital Thing
    #
    def __init__(self, client_id, client_secret, api_key):
        # Self Things
        self.api_key = api_key
        self.client_id = client_id
        self.client_secret = client_secret

        # Gets The Token
        client = BackendApplicationClient(client_id=self.client_id)
        oauth = OAuth2Session(client=client)
        token = oauth.fetch_token(
            token_url="https://backpack.tf/oauth/access_token",
            client_id=self.client_id,
            client_secret=self.client_secret,
        )

        self.token = token

    #
    # Gets a listing by id
    #
    # id - the listing's ID
    #
    def get_listing(self, listing_id=0):
        try:
            client = OAuth2Session(self.client_id, token=self.token)
            r = client.get(
                "https://backpack.tf/api/1.0/classifieds/listings/" + str(listing_id)
            )

        except TokenExpiredError as e:
            token = client.post("https://backpack.tf/oauth/access_token")
            self.token = token

        client = OAuth2Session(self.client_id, token=self.token)
        r = client.get(
            "https://backpack.tf/api/1.0/classifieds/listings/" + str(listing_id)
        )

        return r.text

    # alias for compatibility with older versions
    # please use the new name, "get_listing"
    getListing = get_listing

    #
    # Delete a listing by ID
    #
    # id - the listing's ID
    #
    def delete_listing(self, listing_id=0):
        try:
            client = OAuth2Session(self.client_id, token=self.token)
            r = client.delete(
                "https://backpack.tf/api/1.0/classifieds/listings/" + str(listing_id)
            )

        except TokenExpiredError as e:
            token = client.post("https://backpack.tf/oauth/access_token")
            self.token = token

        client = OAuth2Session(self.client_id, token=self.token)
        r = client.delete(
            "https://backpack.tf/api/1.0/classifieds/listings/" + str(listing_id)
        )

        return r.text

    # alias for compatibility with older versions
    # please use the new name, "delete_listing"
    deleteListing = delete_listing

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
    # returns int: 0 or 1, states the success of the listing
    #
    def create_listing(
        self,
        intent=0,
        id=0,
        quality=6,
        item_name="",
        craftable=1,
        priceindex=0,
        offers=0,
        buyout=1,
        promoted=0,
        details="",
        currencies={"metal": 0},
        account_token="",
    ):
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
                            "priceindex": str(priceindex),
                        },
                        "offers": str(offers),
                        "buyout": str(buyout),
                        "promoted": str(promoted),
                        "details": str(details),
                        "currencies": currencies,
                    }
                ],
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
                        "currencies": currencies,
                    }
                ],
            }

        r = requests.post("https://backpack.tf/api/classifieds/list/v1", json=payload)

        jsonResponse = json.loads(r.text)

        try:
            return int(jsonResponse["listings"][item_name]["created"])
        except:
            return jsonResponse

    # alias for compatibility with older versions
    # please use the new name, "create_listing"
    createListing = create_listing

    #
    # This function searches for classified listings
    #
    # intent - either sell, buy, or both
    # page_size - the results / page 0 < page_size <= 30
    # page - the page number you want to view
    # fold - if set 0 disables listing folding
    # item_name - the name of the item you want to search for
    # steamid - the steam id of the user who you want to check their listings
    # tradable - 0/1
    # craftable - 0/1
    # australium - 0/1
    # wear_tier - 1-5 for tier of skin wear, in order - factory new, minimal wear, field-tested, well-worn, battle scared
    # texture_name - required to search by wear_tier, the name of the skin / texture to search by
    # quality - the integer of the quality to search by use MiscUtils.qualityStringToInt("unique") to get it
    # paint - the paint's ID to search by, TODO: add a function to find the paint ID
    # particle - particle ID effect, TODO: add a function to find the particle ID from string
    # killstreak_tier - 1-3, in order standard, specialized, professional
    # sheen - 0-7, in order team shine, deadly daffodil, manndarin, mean green, agonizing emerald, villainous violet, hot rod
    # killstreaker - the id of the killstreaker
    #
    def search_classifieds(
        self,
        intent="dual",
        page_size=10,
        fold=1,
        item_name="",
        steamid="",
        tradable="",
        craftable="",
        australium="",
        wear_tier="",
        quality="",
        paint="",
        particle="",
        killstreak_tier="",
        sheen="",
        killstreaker="",
        page=0,
        texture_name="",
    ):
        payload = {
            "key": self.api_key,
            "intent": intent,
            "texture_name": texture_name,
            "page": str(page),
            "page_size": str(page_size),
            "fold": str(fold),
            "item": item_name,
            "steamid": str(steamid),
            "tradable": str(tradable),
            "craftable": str(craftable),
            "australium": str(australium),
            "wear_tier": str(wear_tier),
            "quality": str(quality),
            "paint": str(paint),
            "particle": str(particle),
            "killstreak_tier": str(killstreak_tier),
            "sheen": str(sheen),
            "killstreaker": str(killstreaker),
        }

        encoded = urllib.parse.urlencode(payload)

        r = requests.get("https://backpack.tf/api/classifieds/search/v1?" + encoded)
        jsondata = json.loads(r.text)

        return jsondata

    # alias for compatibility with older verisions
    # please use the new function name, "search_classifieds" (lowercase c)
    search_Classifieds = search_classifieds

    #
    # This function extracts the trade url.
    #
    # listingJSON - the JSON object from the search_listings under whatever the listing thing you use is.
    #
    def extract_trade_url(self, listingJSON, proxy=None):
        payload = {
            "item": listingJSON["item"]["name"],
            "steamid": listingJSON["steamid"],
            "quality": listingJSON["item"]["quality"],
        }

        encoded = urllib.parse.urlencode(payload)

        if proxy == None:
            r = requests.get(
                "https://backpack.tf/classifieds?" + encoded.replace("+", "%20")
            )
        else:
            r = requests.get(
                "https://backpack.tf/classifieds?" + encoded.replace("+", "%20"),
                proxies=proxy,
            )

        with open("test.html", "w+", encoding="utf-8") as thing:
            thing.write(r.text)

        tree = html.fromstring(r.text)

        try:
            url = tree.xpath(
                "//li[@id='listing-"
                + listingJSON["id"]
                + "']/div[@class='listing-item']/div"
            )[0].get("data-listing_offers_url")
            return url
        except:
            raise IndexError("List index out of range")
