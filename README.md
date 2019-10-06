
# BackpackTF-API
This is an unoffical api wrapper for the Backpack.tf API in python. You can do a lot with this API keep reading for more information

 [![GitHub release (latest by date)](https://img.shields.io/github/v/release/davidteather/BackpackTf-API)](https://github.com/davidteather/BackpackTf-API/releases) [![GitHub](https://img.shields.io/github/license/davidteather/BackpackTf-API)](https://github.com/davidteather/BackpackTf-API/blob/master/LICENSE) [![PyPI - Downloads](https://img.shields.io/pypi/dm/BackpackTF)](https://pypi.org/project/BackPackTF/)

## Important Information
* If this API stops working for any reason open an issue.
* Feel free to mention @davidteather in an issue you open, because I might not see it otherwise.

## Getting Started

To get started using this api follow the instructions below.

You need to register for an API key and create an app to use all the fucntions of this api at [BackpackTF](https://backpack.tf/developer)

### Installing

If you need help installing or run into some error, please open an issue. I will try to help out as much as I can.

Tested with python 3.7.3

```
pip install BackpackTF
```

## Quick Start Guide

Here's a quick bit of code to get an item's price

```
from BackpackTF import Currency

api = Currency(apikey="xxxxxxxxxxxxxxxxx")

price = api.itemPrice(name="Tour of Duty Ticket", quality="Unique", craftable=1, tradable=1)

print(price)
```

## Detailed Documentation

### The Account Class

__init__


| Attributes    | Description   |
| ------------- | ------------- |
| client_id     | from your backpack.tf app [here](https://backpack.tf/developer/apps) |
| client_secret | from your backpack.tf app [here](https://backpack.tf/developer/apps) |
| api_key       | your api key from [here](https://backpack.tf/developer/apikey/view)  |


#### createListing - creates a listing / classified on backpack.tf


| Attributes    | Description   |
| ------------- | ------------- |
| intent     | 0 (Buy) or 1 (Sell) |
| id | if intent is 1, the current id of the id you want to list |
| item_name       | if intent is 0, the item's name you want to buy |
| quality       | if intent is 0, either the number or the text |
| craftable       | if intent is 0, 0 or 1 |
| offers       | set to 0 for only accepting friend requests |
| buyout       | set to 0 to allow negotiation |
| promoted       | set to 1 to promote it, must be premium |
| details       | the listing comment, max 200 characters |
| priceindex       | complicated, most of the time is 0. [More info](https://image.prntscr.com/image/-zjCD9FiS0ijpGHtG8gNBA.png) |

returns 0 or 1 for success or failure.


#### search_classifieds - searches for classifieds


| Attributes    | Description   |
| ------------- | ------------- |
| intent     | either sell, buy, or both |
| page_size     | the results / page 0 < page_size <= 30 |
| page     | the page number you want to view |
| fold     | if set 0 disables listing folding |
| item_name     | the name of the item you want to search for |
| steamid     | the steam id of the user who you want to check their listings |
| tradable     | 0/1 |
| craftable   | 0/1 |
| australium  | 0/1 |
| wear_tier  | 1-5 for tier of skin wear, use MiscUtils().wear_Tier_String_To_Int() |
| texture_name  | required to search by wear_tier, the name of the skin / texture to search by |
| quality  | the integer of the quality to search by use MiscUtils().qualityStringToInt() to get it |
| paint  | the paint's ID to search by |
| particle  | particle ID effect |
| killstreak_tier  | 1-3, use MiscUtils().killstreaker_Tier_String_To_Int() |
| sheen  | 0-7, use MiscUtils().sheen_String_To_Int() |
| killstreaker  | the id of the killstreaker |

returns a dictionary. [Here](https://gist.github.com/davidteather/109acc0acd7e7d59f8192d8d8cfcba7c)'s an example json


#### extract_trade_url - extracts the trade url with token from a listing


| Attributes    | Description   |
| ------------- | ------------- |
| listingJSON   | This is the json object of a classified listing on backpack.tf. You can get this using the method above. |
| proxy     | This is an optional field, provide a dictionary that fits the python requests module requirements. See [here](https://stackoverflow.com/questions/8287628/proxies-with-python-requests-module) |


returns the trade url as a string.


### The Currency Class

__init__


| Attributes    | Description                                                         |
| ------------- | ------------------------------------------------------------------- |
| apikey        | your api key from [here](https://backpack.tf/developer/apikey/view) |


#### getCurrencies - gets currency values


| Attributes    | Description   |
| ------------- | ------------- |
| None       | None  |

returns a dictonary. [Here's](https://gist.github.com/davidteather/4f9c82f3d224e64c3a187ad28db26d1a) an example json.


#### priceHistory - gets the price history for a given item


| Attributes    | Description   |
| ------------- | ------------- |
| name       | the name of the item you want to search for  |
| quality  | the integer of the quality to search by use MiscUtils().qualityStringToInt("unique") to get it |
| craftable       | 0/1  |
| tradable       | 0/1  |
| priceindex       | complicated, most of the time is 0. [More info](https://image.prntscr.com/image/-zjCD9FiS0ijpGHtG8gNBA.png) |

returns an array of dictionaries. [Here's](https://gist.github.com/davidteather/db87fbe0bfd7d0ac88cb5412d1bba878) an example.


#### itemPrice - gets the current price for a given item


| Attributes    | Description   |
| ------------- | ------------- |
| name       | the name of the item you want to search for  |
| quality  | the integer of the quality to search by use MiscUtils().qualityStringToInt("unique") to get it |
| craftable       | 0/1  |
| tradable       | 0/1  |
| priceindex       | complicated, most of the time is 0. [More info](https://image.prntscr.com/image/-zjCD9FiS0ijpGHtG8gNBA.png) |

returns a single dictionary of current value. [Here's](https://gist.github.com/davidteather/a791078ef11d6977d7a9b77d249bd78e) an example.


#### getAllPrices - gets all prices


| Attributes    | Description   |
| ------------- | ------------- |
| raw       | shows a value_low field   |
| since  | will only show items that has had price changes since the unix epoch. |

returns a kind of weird json file. [Here's](https://gist.github.com/davidteather/eefde719b1ac0031656acbacc4a614c8) an example, and [here's](https://gist.github.com/davidteather/9a8fc5c7bfa6a484b8f28785ee30c6dd) the structure.


### The MiscUtils Class

__init__


| Attributes    | Description   |
| ------------- | ------------- |
| None          | None          |


#### quality_String_To_Int


| Attributes    | Description   |
| ------------- | ------------- |
| string        | The string of the quality. Ex: "unique"  |


#### particle_String_To_Int


| Attributes    | Description   |
| ------------- | ------------- |
| string        | The string of the particle effect. |


#### rarity_String_To_Int


| Attributes    | Description   |
| ------------- | ------------- |
| string        | The string of the rarity.  |


#### origin_String_To_Int


| Attributes    | Description   |
| ------------- | ------------- |
| string        | The string of the origin. |


#### wear_tier_String_To_Int


| Attributes    | Description   |
| ------------- | ------------- |
| string        | The string of the wear_tier. |


#### killstreaker_String_To_Int


| Attributes    | Description   |
| ------------- | ------------- |
| string        | The string of the killstreaker. |


#### strange_parts_String_To_Int


| Attributes    | Description   |
| ------------- | ------------- |
| string        | The string of the strange part. |


#### steam_id_to_account_id


| Attributes    | Description   |
| ------------- | ------------- |
| string        | The string of the steam_id.  |

returns an int of the account id.

## Built With

* [Python 3.7](https://www.python.org/) - The web framework used

## Authors

* **David Teather** - *Initial work* - [davidteather](https://github.com/davidteather)

See also the list of [contributors](https://github.com/davidteather/BackpackTF-API/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
