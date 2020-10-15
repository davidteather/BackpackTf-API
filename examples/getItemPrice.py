from BackpackTF import Currency

api = Currency(apikey="xxxxxxxxxxxxxxxxx")

price = api.itemPrice(
    item="Tour of Duty Ticket", quality="Unique", craftable=1, tradable=1, priceindex=0
)

print(price)
