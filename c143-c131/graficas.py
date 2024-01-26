import csv
import plotly.express as px

rows = []

with open("main.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        rows.append(row)

    headers = rows[0]
    planet_data_rows = rows[1:]
    print(headers)
    print(planet_data_rows[0])

solar_system_planet_count = {}

for planet_data in planet_data_rows :
    if solar_system_planet_count.get(planet_data[10]):
        solar_system_planet_count[planet_data[10]]+=1
    else:
        solar_system_planet_count[planet_data[10]] = 1

# En síntesis, revisa si el sistema planetario existe, si es así incrementa el contador o lo agrega con un planeta
# [
#     tierra, SolarSystem
#     Marte, SolarSystem
#     Alpha, Centaurus
#     Beta, Centaurus
#     Sigma, UrsaMinor
# ]

# counter = {"SolarSystem": 2, "Centaurus": 2, "UrsaMinor":1}
print(solar_system_planet_count)

max_solar_system = max(solar_system_planet_count, key=solar_system_planet_count.get)
print("Sistema solar con más planetas:", max_solar_system)
print("Número de planetas:", solar_system_planet_count.get(max_solar_system))

temp_planet_data_rows = list(planet_data_rows)

for planet_data in temp_planet_data_rows:
    planet_mass = planet_data[2]

    if planet_mass.lower() == "unknown":
        planet_data_rows.remove(planet_data)
        continue
    else:
        planet_mass_value = planet_mass.split(" ")[0]
        planet_mass_ref = planet_mass.split(" ")[1]
        if planet_mass_ref == "Jupiters":
            planet_mass_value = float(planet_mass_value) * 317.8
        planet_data[2] = planet_mass_value

    planet_radius = planet_data[5]

    if planet_radius.lower() == "unknown":
        planet_data_rows.remove(planet_data)
        continue
    else:
        planet_radius_value = planet_radius.split(" ")[0]
        planet_radius_ref = planet_radius.split(" ")[2]
        if planet_radius_ref == "Jupiters":
            planet_radius_value = float(planet_radius_value) * 11.2
        planet_data[5] = planet_radius_value

print("Cuntos planetas quedan:", len(planet_data_rows))

koi_351_planets = []
for planet_data in planet_data_rows:
    if max_solar_system == planet_data[10]:
        koi_351_planets.append(planet_data)

print("Cuántos planetas hay en Koi:", len(koi_351_planets))
print(koi_351_planets)

koi_351_planet_masses = []
koi_351_planet_names = []

for planet_data in koi_351_planets:
    koi_351_planet_masses.append(planet_data[2])
    koi_351_planet_names.append(planet_data[9])
    
koi_351_planet_masses.append(1)
koi_351_planet_names.append("Tierra")

fig = px.bar(x=koi_351_planet_names, y=koi_351_planet_masses)
fig.update_layout(yaxis={'categoryorder':'category ascending'})
fig.show()
 
headers[0] = "row_num"

max_solar_system = max(solar_system_planet_count, key=solar_system_planet_count.get)
print("¡El sistema solar {} tiene el máximo número de planetas {} de todos los sistemas solares que hemos descubierto hasta ahora!".format(max_solar_system, solar_system_planet_count[max_solar_system]))    

temp_planet_data_rows = list(planet_data_rows)
for planet_data in temp_planet_data_rows:
  if planet_data[0].lower() == "hd 100546 b":
    planet_data_rows.remove(planet_data)

planet_masses = []
planet_radiuses = []
planet_names = []
for planet_data in planet_data_rows:
  planet_masses.append(planet_data[2])
  planet_radiuses.append(planet_data[5])
  planet_names.append(planet_data[0])
planet_gravity = []
for index, name in enumerate(planet_names):
  gravity = (float(planet_masses[index])*5.972e+24) / (float(planet_radiuses[index])*float(planet_radiuses[index])*6371000*6371000) * 6.674e-11
  planet_gravity.append(gravity)

fig = px.scatter(x=planet_radiuses, y=planet_masses, size=planet_gravity, hover_data=[planet_names])
fig.show()

low_gravity_planets = []
for index, gravity in enumerate(planet_gravity):
  if gravity < 100:
    low_gravity_planets.append(planet_data_rows[index])

print(len(low_gravity_planets))