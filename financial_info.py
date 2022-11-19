import requests
from bs4 import BeautifulSoup


#function to get financial information of a perticular company by their symbol
def getFinancialInformation(symbol):
    furl = "https://finance.yahoo.com/quote/"+symbol+"?p="+symbol
    response = requests.get(furl)

    soup = BeautifulSoup(response.text, features="html.parser")

    finalName = "1y Target Est"
    trs = soup.find_all("tr")
    names = []
    values = []
    namval = {}

    

    for i in range(len(trs)):
        for j in range(len(trs[i].contents)):
            global name
            global value
            if j == 0:
                try:
                    name = trs[i].contents[j].text
                    names.append(name)
                except:
                    continue
            if j == 1:
                try:
                    value = trs[i].contents[j].text
                    values.append(value)
                except:
                    continue
        namval[name] = value
        if name == finalName:
            break
    return namval

#function to get company list by their symbols
def getCompanyList():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

    response = requests.get(url)

    t = response.text
    soup = BeautifulSoup(t, features="html.parser")
    tbody = soup.find_all("tbody")

    Symbol_list = []

    for i in range(len(tbody[0].contents)):
        if i < 2:
            continue
        if i % 2 != 0:
            continue
        Symbol_list.append(tbody[0].contents[i].contents[1].text.strip("\n"))

    return Symbol_list


tickerSymbols = getCompanyList()

# Top 10 S&P 500 companies data
for i in range(10):
    print(tickerSymbols[i],getFinancialInformation(tickerSymbols[i]))
   


