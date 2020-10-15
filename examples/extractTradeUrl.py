from BackpackTF.account import Account

user = Account(client_id="xxxxxx", client_secret="xxxxxx", api_key="xxxxxx")

classifieds = user.search_Classifieds()["buy"]["listings"]

for classified in classifieds:
    trade_url = user.extract_trade_url(classified)
    print(trade_url)
