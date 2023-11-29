from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import csv

START_URL = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"

browser = webdriver.Chrome()
browser.get(START_URL)
soup = BeautifulSoup(browser.page_source,"html.parser")

#Explicar qué hace bs4 y el webdriver
# file = open("index.html", "w")
# file.write(str(soup)) 
# file.close()
# print(soup)

# print(soup.find_all("ul", attrs={"class", "exoplanet"}))

#tabla_pag1 = soup.find_all("ul", attrs={"class", "exoplanet"})
#planeta1 = tabla_pag1[0]
total_pages = int(soup.find_all("span", attrs={"class", "total_pages"})[0].contents[0])
print(total_pages)
time.sleep(10)

def scrape():
    headers = ["name", "ligh_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]
    planet_data = []
    for i in range(0,total_pages):
        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
        browser.find_element(By.XPATH, '//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    print(headers)
    print(planet_data[1])

    with open("list_of_planets.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
scrape()

