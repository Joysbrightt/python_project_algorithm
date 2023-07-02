# hash_tables are also known as hash maps, maps, dictionaries, and
# associative arrays.
from linecache import cache

book = dict()

book["apple"] = 1
book["milk "] = 2
book["avocado"] = 3
book["butter"] = 4
# print(book)
#
# print(book["avocado"])

# todo another example of using an hashtable

phone_book = {}
phone_book["tomi"] = 8139166146
phone_book["emergency"] = 911
print(phone_book)


# print(phone_book["tomi"])


# # todo hashtable in cache
#
# def get_page(url):
#     if cache.get(url):
#         return cache[url]
#     else:
#         data = get_data_from_server(url)
#         cache[url] = data
#         return data
