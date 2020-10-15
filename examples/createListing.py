from BackpackTF.account import Account

# Get these attributes from backpack.tf/developer
user = Account(client_id="xxxxxxxxx", client_secret="xxxxxxxxxx", api_key="xxxxxxxxxx")


print(
    user.createListing(
        intent=0,
        id=0,
        quality=6,
        item_name="Tour of Duty Ticket",
        craftable=1,
        priceindex=0,
        offers=1,
        buyout=1,
        promoted=0,
        details="",
        currencies={"metal": "23"},
        account_token="xxxxxxxxxxxxxxxxx",
    )
)
