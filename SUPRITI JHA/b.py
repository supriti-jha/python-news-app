# import a

# a.sum(4,5)

# import random as r
# import math as m

# print(r) # r.random() 0 - 1

# print(m.ceil(r.random()*10))


# import requests as r
# import pandas as psd
# import openpyxl

# data = r.get("https://newsapi.org/v2/everything?q=tesla&from=2025-02-01&sortBy=publishedAt&apiKey=1613ce0ed54744078f27cba62aa91796")

# print(data.status_code)

# jsondata = data.json()['articles']

# df = psd.DataFrame(jsondata)
# df.to_excel('supritis.xlsx', index=False)

# def fun():
#     """helo world here my  name"""
#     print('heo world')


# print(fun.__doc__)



# import requests as r
# import pandas as psd
# import openpyxl
# data = r.get("https://newsapi.org/v2/everything?q=tesla&from=2025-02-01&sortBy=publishedAt&apiKey=1613ce0ed54744078f27cba62aa91796")

# print(data.status_code)

# jsondata = data.json()['articles']

# df = psd.DataFrame(jsondata)
# df.to_excel('supritis.xlsx', index=False)

a = {"name":"saif", "email":"saf@gmail.com"}


for x in a:
    print(a[x])
