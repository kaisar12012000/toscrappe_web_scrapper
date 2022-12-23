import requests
from bs4 import BeautifulSoup
import xlsxwriter
import uuid

def makeSpreadSheet ():
    file_name = uuid.uuid4()
    workbook = xlsxwriter.Workbook(f"{file_name}.xlsx")

    worksheet = workbook.add_worksheet()

    worksheet.write("A1", "Name of the book")
    worksheet.write("B1", "Price in pounds")
    worksheet.write("C1", "Status")
    worksheet.write("D1", "Rating out of 5")

    return worksheet, workbook

def addData(name, price, stat, rtg, row, ws):
    ws.write(f"A{row}", name)
    ws.write(f"B{row}", price)
    ws.write(f"C{row}", stat)
    ws.write(f"D{row}", rtg)

mapp = {
    "One" : 1,
    "Two" : 2,
    "Three" : 3,
    "Four" : 4,
    "Five": 5
}

if __name__ == "__main__":
    req = requests.get("http://books.toscrape.com/")



    soup = BeautifulSoup(req.content, "html.parser")

    # title = soup.title

    opp = soup.find_all('article', { "class" : "product_pod" })

    sheet, workbook = makeSpreadSheet()
    row = 2
    for article in opp:
        name = article.find("h3").text
        price = article.find_all("p", {"class":"price_color"})[0].text
        status = article.find_all("p", {"class":"availability"})[0].text
        rating = mapp[article.find_all("p", {"class" : "star-rating"})[0]["class"][1]]
        addData(name, price, status, rating, row, sheet)
        row+=1

    workbook.close()
        
# print(opp)

# print(soup.prettify())

