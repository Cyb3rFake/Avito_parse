# import datetime
# from collections import namedtuple
# from fake_useragent import UserAgent

# import bs4
# import requests


# headers = {'User-Agent': UserAgent().random,'Accept-Language': 'ru'}
# print(headers)
# InnerBlock = namedtuple('Block', 'title,price,currency,date,url')

# class Block(InnerBlock):
#     def __str__(self) -> str:
#         return f'{self.title}\
#             \t{self.price}\
#                 {self.currency}\
#                     \t{self.date}\
#                         \t{self.url}'
    
# class AvitoParser:

#     def __init__(self) -> None:
#         self.session = requests.Session()
#         self.session.headers = headers
    
#     def get_page(self, page: int = None):
#         params = {
            
#         }

str = "https://www.avito.ru/lipetsk?p=100&q=%D0%B4%D0%BE%D0%BC%D0%B0"

print(str.find("="),str.find("&"))
print(str[str.find("=")+1:str.find("&")])