import csv

rows = []

with open("main.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        rows.append(row)

headers = rows[0]
planet_data_rows = rows[1:]

print("Cabeceras y primer planeta")
print(headers)
print(planet_data_rows[0])

#contamos los planetas en los sistemas solares
solar_system_planet_count = {}

for planet_data in planet_data_rows :
    if solar_system_planet_count.get(planet_data[11]):
        solar_system_planet_count[planet_data[11]]+=1
    else:
        solar_system_planet_count[planet_data[11]] = 1

print(solar_system_planet_count)

# Buscamos el sistema solar con más planetas
max_solar_system = max(solar_system_planet_count, key=solar_system_planet_count.get)
print("Sistema solar con más planetas:", max_solar_system)
print("Número de planetas:", solar_system_planet_count.get(max_solar_system))

# Normalizamos los datos a la masa de la tierra, si aparecen los datos como júpiter
# los multiplicamos por las veces que cabe la tierra
# Así tenemos todos los datos con base en los de la tierra
temp_planet_data_rows = list(planet_data_rows)
for planet_data in temp_planet_data_rows:
  planet_mass = planet_data[3]
  if planet_mass.lower() == "unknown":
    planet_data_rows.remove(planet_data)
    continue
  else:
    planet_mass_value = planet_mass.split(" ")[0]
    planet_mass_ref = planet_mass.split(" ")[1]
    if planet_mass_ref == "Jupiters":
      planet_mass_value = float(planet_mass_value) * 317.8
    planet_data[3] = planet_mass_value

  planet_radius = planet_data[7]
  if planet_radius.lower() == "unknown":
    planet_data_rows.remove(planet_data)
    continue
  else:
    planet_radius_value = planet_radius.split(" ")[0]
    planet_radius_ref = planet_radius.split(" ")[2]
    if planet_radius_ref == "Jupiter":
      planet_radius_value = float(planet_radius_value) * 11.2
    planet_data[7] = planet_radius_value

print(len(planet_data_rows))

# Como sabemos que Koi_251 tiene más planetas, obtendremos los datos de su masa y los grtaficaremos
koi_351_planets = []
for planet_data in planet_data_rows:
  if max_solar_system == planet_data[11]:
    koi_351_planets.append(planet_data)

print(len(koi_351_planets))
print(koi_351_planets)

import plotly.express as px

koi_351_planet_masses = []
koi_351_planet_names = []
for planet_data in koi_351_planets:
  koi_351_planet_masses.append(planet_data[3])
  koi_351_planet_names.append(planet_data[1])

koi_351_planet_masses.append(1)
koi_351_planet_names.append("Tierra")

fig = px.bar(x=koi_351_planet_names, y=koi_351_planet_masses)
#fig.show()

temp_planet_data_rows = list(planet_data_rows)
for planet_data in temp_planet_data_rows:
  if planet_data[1].lower() == "hd 100546 b":
    planet_data_rows.remove(planet_data)

# Se grafican los planetas según su gravedad (Radio del círculo) Colocándose según
# Su masa y su radio
planet_masses = []
planet_radiuses = []
planet_names = []
for planet_data in planet_data_rows:
  planet_masses.append(planet_data[3])
  planet_radiuses.append(planet_data[7])
  planet_names.append(planet_data[1])
planet_gravity = []
for index, name in enumerate(planet_names):
  gravity = (float(planet_masses[index])*5.972e+24) / (float(planet_radiuses[index])*float(planet_radiuses[index])*6371000*6371000) * 6.674e-11
  planet_gravity.append(gravity)

fig = px.scatter(x=planet_radiuses, y=planet_masses, size=planet_gravity, hover_data=[planet_names])
#fig.show()

# Buscamos planetas con menor gravedad (Menos que 100 veces la gravedad de la tierra)

low_gravity_planets = []
for index, gravity in enumerate(planet_gravity):
  if gravity < 100:
    low_gravity_planets.append(planet_data_rows[index])

print("Planetas con gravedad soportable:",len(low_gravity_planets))

planet_type_values = []
# planet_type_values_gabo = []

for planet_data in planet_data_rows :
    planet_type_values.append(planet_data[6])

    # if planet_data[6] in planet_type_values_gabo :
    #     continue
    # else :
    #     planet_type_values_gabo.append(planet_data[6])

print("Tipos de planetas")
print(list(set(planet_type_values)))
# print(planet_type_values_gabo)

planet_masses = []
planet_radiuses = []

for planet_data in low_gravity_planets:
   planet_masses.append(planet_data[3])
   planet_radiuses.append(planet_data[7])

fig = px.scatter(x=planet_radiuses, y=planet_masses)
#fig.show()


from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

X = []
for index, planet_mass in enumerate(planet_masses):
  temp_list = [
                  planet_radiuses[index],
                  planet_mass
              ]
  X.append(temp_list)

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state = 42)
    kmeans.fit(X)
    # Método 'inertia' regresa el wcss para ese modelo.
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(10,5))
sns.lineplot(x=range(1, 11), y=wcss, marker='o', color='red')
plt.title('El método del codo')
plt.xlabel('Número de grupos')
plt.ylabel('WCSS')
#plt.show()



planet_types = []

for planet_data in low_gravity_planets :
   planet_types.append(planet_data[6])

fig = px.scatter(x=planet_radiuses, y=planet_masses, color=planet_types)
#fig.show()

suitable_planets = []

for planet_data in low_gravity_planets:
   if planet_data[6].lower() == "terrestrial" or planet_data[6].lower() == "super earth" :
      suitable_planets.append(planet_data)

print("Cantidad de planetas probablemente habitables", len(suitable_planets))

print(headers)

#print(len(suitable_planets))

temp_suitable_planets = list(suitable_planets)

for planet_data in temp_suitable_planets:
   if planet_data[8].lower() == "unknown":
      suitable_planets.remove(planet_data)

#print(len(suitable_planets))

for planet_data in suitable_planets:
  if planet_data[9].split(" ")[1].lower() == "days":
    planet_data[9] = float(planet_data[9].split(" ")[0]) #Días
  else:
    planet_data[9] = float(planet_data[9].split(" ")[0])*365 #Años
  
  planet_data[8] = float(planet_data[8].split(" ")[0])
   

orbital_radiuses = []
orbital_periods = []

for planet_data in suitable_planets:
   orbital_radiuses.append(planet_data[8])
   orbital_periods.append(planet_data[9])

fig = px.scatter(x=orbital_radiuses, y=orbital_periods)
fig.show()

goldilock_planets = list(suitable_planets)

temp_goldilock_planets = list(suitable_planets)
for planet_data in list(suitable_planets) :
   if planet_data[8] < 0.38 or planet_data[8] > 2 :
      goldilock_planets.remove(planet_data)

print("Planetas con información de velocidad y radio:", len(suitable_planets))
print("Planetas en la zona Ricitos de Oro", len(goldilock_planets))

planet_speeds = []

for planet_data in suitable_planets :
   distance = 2 * 3.14 * (planet_data[8] * 1.496e+8)
   time = planet_data[9] * 86400
   speed = distance / time
   planet_speeds.append(speed)

speed_supporting_planets = list(suitable_planets)

temp_speed_supportint_planets = list(suitable_planets)
for index, planet_data in enumerate(suitable_planets) :
   if planet_speeds[index] > 200:
      speed_supporting_planets.remove(planet_data)

print("Planetas con la velocidad adecuada:",len(speed_supporting_planets))

goldilock_speed_planets = []
for planet_data in goldilock_planets :
   distance = 2 * 3.14 * (planet_data[8] * 1.496e+8)
   time = planet_data[9] * 86400
   speed = distance / time
   goldilock_speed_planets.append(speed)

temp_goldilock_speed_planets = list(goldilock_speed_planets)
for index, planet_data in enumerate(temp_goldilock_speed_planets) :
   if planet_speeds[index] > 200:
      goldilock_speed_planets.remove(planet_data)

print("Planetas con la velocidad adecuada dentro de la zona Ricitos de Oro:",len(goldilock_speed_planets))
