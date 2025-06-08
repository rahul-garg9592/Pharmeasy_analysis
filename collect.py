from bs4 import BeautifulSoup
import os
import pandas as pd
#solve the error  html_doc = f.read()
#   File "<frozen codecs>", line 325, in decode
#UnicodeDecodeError: 'utf-8' codec can't decode byte 0x80 in position 3131: invalid start byte
d = {"test_name": [], "test_MRP_price": [],"test_discounted_price": [], "test_description": []}
for file in os.listdir("data"):
    with open(f"data/{file}", "r", encoding="utf-8", errors='ignore') as f:
        html_doc = f.read()
    soup = BeautifulSoup(html_doc, "html.parser")
    test_name = soup.find("h2").text if soup.find("h2") else "No Title"
    test_MRP_price = soup.find("span", class_="sc-b6bb78f6-6").text if soup.find("span", class_="sc-b6bb78f6-6") else "No MRP Price"
    test_discounted_price = soup.find("span", class_="sc-b6bb78f6-3").text if soup.find("span", class_="sc-b6bb78f6-3") else "No Discounted Price"
    test_description = soup.find("span", class_="sc-28344409-8").text if soup.find("span", class_="sc-28344409-8") else "No Description"
    d["test_name"].append(test_name)
    d["test_MRP_price"].append(test_MRP_price)
    d["test_discounted_price"].append(test_discounted_price)
    d["test_description"].append(test_description)

# Create a DataFrame
df = pd.DataFrame(d)
df.to_csv("tests_data.csv", encoding="utf-8")
