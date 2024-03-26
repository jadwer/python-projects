from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


bright_stars_url = 'https://en.wikipedia.org/w/index.php?title=List_of_brightest_stars_and_other_record_stars&direction=next&oldid=1187363889'

page = requests.get(bright_stars_url)
print("print page:", page)

soup = bs(page.text,'html.parser')

star_table = soup.find_all('table')


temp_list= []
table_rows = star_table[1].find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)


Star_names = []
Distance =[]
Mass = []
Radius =[]
Lum = []

for i in range(1,len(temp_list)):
    Star_names.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])
    Lum.append(temp_list[i][7])
    
df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,Lum)),columns=['Star_name','Distance','Mass','Radius','Luminosity'])
print(df2)

df2.to_csv('bright_stars.csv')

""" 
nombres = ["Juan", "Anna", "Pedro"]
edades = [8, 10, 11]

alumnos = zip(nombres, edades)
print("alumnos: ",alumnos)
print("alumnos en lista: ", list(alumnos))

 """
 
# alumnos[(nombre, edad)]