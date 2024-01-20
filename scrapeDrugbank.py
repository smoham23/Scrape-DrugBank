#Author: Shadi Mohammadabadi

from bs4 import BeautifulSoup
import requests
import csv
import re

# Create a data dictionary to store the data
data = {}


with open("./ID_list.txt", "r") as f:
    for line in f:
        ID = line.strip()

        # Step 1: Sending a HTTP request
        url = "https://go.drugbank.com/drugs/"+ID
        
        # Make a GET request to fetch the raw HTML content
        html_content = requests.get(url).text

        # Step 2: Parse the HTML content
        soup = BeautifulSoup(html_content, "lxml")
        #print(soup.prettify())
        
        # Step 3: Analyze the HTML tag
        # Get the text having the desired class
        try:        
            header = soup.find("h1", attrs={"class":"align-self-center mr-4"}).text
            data[ID] = header
        except AttributeError:
            data[ID] = "drug " + ID

try:
    with open("./ID_name.csv", 'w') as csvfile:
        for key in data.keys():
            csvfile.write("%s,%s\n"%(key,data[key]))
except IOError:
    print("I/O error")

