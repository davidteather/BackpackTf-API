from BackpackTF import Currency

api = Currency(apikey="xxxxxxxxxxxxxxxxx")

price = api.itemPrice(
    name="Tour of Duty Ticket", quality="Unique", craftable=1, tradable=1
)

print(price)
