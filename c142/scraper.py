from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import csv

START_URL = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"

browser = webdriver.Chrome()
browser.get(START_URL)
soup = BeautifulSoup(browser.page_source,"html.parser")

total_pages = int(soup.find_all("span", attrs={"class", "total_pages"})[0].contents[0])
print(total_pages)
time.sleep(2)
headers = ["name", "ligh_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date", "hyperlink", "planet_type", "planet_radius", "orbital_radius", "orbital_period", "eccentricity"]
planet_data = []
new_planet_data=[]

def scrape():
    for i in range(1,2):
    # for i in range(1,2):

        while True:
            time.sleep(0.25)
            soup = BeautifulSoup(browser.page_source, "html.parser")
            current_page_num = int(soup.find_all("input", attrs={"class", "page_num"})[0].get("value"))
            if current_page_num < i:
                browser.find_element(By.XPATH,'//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
            elif current_page_num > i:
                browser.find_element(By.XPATH,'//*[@id="primary_column"]/footer/div/div/div/nav/span[1]/a').click()
            else:
                break
                

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
            hyperlink_li_tag = li_tags[0]
            hyperlink = "https://exoplanets.nasa.gov"+hyperlink_li_tag.find_all("a", href=True)[0]["href"]
            temp_list.append(hyperlink)
            planet_data.append(temp_list)
            #  planet_data.extend(scrape_more_data(hyperlink))
        browser.find_element(By.XPATH, '//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
        print(f"Extracción de datos de la página {i} completada")


def scrape_more_data(hyperlink):
    try:
        page = requests.get(hyperlink)
        soup = BeautifulSoup(page.content, "html.parser")
        temp_list = []

        for tr_tag in soup.find_all("tr", attrs={"class": "fact_row"}):
            td_tags = tr_tag.find_all("td")
            for td_tag in td_tags:
                try:
                    temp_list.append(td_tag.find_all("div", attrs={"class": "value"})[0].contents[0])
                except:
                    temp_list.append("")
        description = soup.find_all("div", attrs={"class":"wysiwyg_content"})[0].contents[0]
        new_planet_data.append(description)
        new_planet_data.append(temp_list)
    except:
        time.sleep(1)
        scrape_more_data(hyperlink)

scrape()
print(planet_data)

for index, data in enumerate(planet_data):
    scrape_more_data(data[5])
    print(f"Datos extraídos del hipervínculo {index + 1} completado 2")

final_planet_data = []
for index, data in enumerate(planet_data):
    new_planet_data_element = new_planet_data[index]
    new_planet_data_element = [elem.replace("\n", "") for elem in new_planet_data_element]
    new_planet_data_element = new_planet_data_element[:7]
    final_planet_data.append(data + new_planet_data_element)

    with open("list_of_planets.csv", "w", newline='') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(final_planet_data)
