# import tabula
# import pandas as pd

# data = tabula.read_pdf("hdfc.pdf", pages="all")
# data = data.dropna(axis="columns")
# print(data)




# tabula.convert_into("hdfc.pdf", "Generatehdfc.csv", pages="all", output_format="csv")

import pdftables_api

conversion = pdftables_api.Client('tt77exakdbhk')

conversion.csv('hdfc.pdf', 'aaa.csv')