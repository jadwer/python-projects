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

print("Número de planetas después de quitar los valores desconocidos", len(planet_data_rows))

# Como sabemos que Koi_251 tiene más planetas, obtendremos los datos de su masa y los grtaficaremos
koi_351_planets = []
for planet_data in planet_data_rows:
  if max_solar_system == planet_data[11]:
    koi_351_planets.append(planet_data)

print("Planetas en KOI:", len(koi_351_planets))
#print("Datos de los planetas en Koi:", koi_351_planets)

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
print("Gráfica de barra de la masa de los planetas en koi")
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
print("Gráfica de los planetas según su radio y masa, visualizando su gravedad según la circunferencia")

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
print("Grafica de la masa y radio de planetas con poca gravedad")


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
print("Se imprimen los conjuntos encontrados por kmeans")



planet_types = []

for planet_data in low_gravity_planets :
   planet_types.append(planet_data[6])

fig = px.scatter(x=planet_radiuses, y=planet_masses, color=planet_types)
#fig.show()
print("Graficamos con código de colores los tipos de planetas")

suitable_planets = []

for planet_data in low_gravity_planets:
   if planet_data[6].lower() == "terrestrial" or planet_data[6].lower() == "super earth" :
      suitable_planets.append(planet_data)

print("Cantidad de planetas probablemente habitables", len(suitable_planets))

#print(headers)

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
print("Graficamos los planetas según su radio y periodo orbital")

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
#-----------------------------------------------------------------
#-----------------------------------------------------------------
# goldilock_speed_planets = []
# for planet_data in goldilock_planets :
#    distance = 2 * 3.14 * (planet_data[8] * 1.496e+8)
#    time = planet_data[9] * 86400
#    speed = distance / time
#    goldilock_speed_planets.append(speed)

# temp_goldilock_speed_planets = list(goldilock_speed_planets)
# for index, planet_data in enumerate(temp_goldilock_speed_planets) :
#    if planet_speeds[index] > 200:
#       goldilock_speed_planets.remove(planet_data)

# print("Planetas con la velocidad adecuada dentro de la zona Ricitos de Oro:",len(goldilock_speed_planets))

#-----------------------------------------------------------------
#-----------------------------------------------------------------

habitable_planets = []
for planet in speed_supporting_planets:
   if planet in goldilock_planets : 
      habitable_planets.append(planet)

print("Los planetas en en la lista ricitos de oro que tienen velocidad aceptable son:", len(habitable_planets))

final_dict = {}

for index, planet_data in enumerate(planet_data_rows):
   features_list = []
   gravity = (float(planet_data[3])*5.972e+24) / (float(planet_data[7])*float(planet_data[7])*6371000*6371000) * 6.674e-11

# Si la gravedad del planeta está dentro de lo aceptable, le agregamos la característica gravedad a la lista
   try:
      if gravity < 100:
         features_list.append("gravity")
   except : pass

# Si es el tipo terrestrial o super-tierra, le agregamos la característica tipo de planeta a la lista
   try :
      if planet_data[6].lower() == "terrestrial" or planet_data[6].lower() == "super earth" :
         features_list.append("planet_type")
   except: pass
# Si está dentro del rango Ricitos de Oro, le agregamos la característica goldilock a la lista
   try :
      if planet_data[8] > 0.38 or planet_data[8] < 2 :
         features_list.append("goldilock")
   except: pass
# Si tiene una velocidad aceptable, le agregamos la caracterísitica speed a la lista
   try :
      distance = 2 * 3.14 * (planet_data[8]*1.496e+8)
      time = planet_data[9] * 86400
      speed = distance / time
      if speed < 200 :
         features_list.append("speed")
   except: pass
   final_dict[index] = features_list
print("Diccionario de características de los planetas")
#print(final_dict)

goldilock_planet_count = 0
for key, value in final_dict.items():
  if "goldilock" in value:
    goldilock_planet_count += 1

print("Planetas dentro del rango Ricitos de Oro:", goldilock_planet_count)

speed_planet_count = 0
for key, value in final_dict.items():
  if "speed" in value:
    speed_planet_count += 1

print("Planetas que cumplen con la velocidad: ", speed_planet_count)

gravity_planet_count = 0
for key, value in final_dict.items():
   if "gravity" in value:
      gravity_planet_count += 1

print("Planetas encontrados con la característica \"Gravity\":", gravity_planet_count)

type_planet_count = 0
for key, value in final_dict.items():
   if "planet_type" in value:
      type_planet_count += 1

print("Los planetas con la característica \"Type_planet\" son:", type_planet_count)

planet_not_gravity_support = []
for planet_data in planet_data_rows : 
   if planet_data not in low_gravity_planets:
      planet_not_gravity_support.append(planet_data)
  
type_no_gravity_planet_count = 0
for planet_data in planet_not_gravity_support:
   if planet_data[6].lower() == "terrestrial" or planet_data[6].lower() == "super earth":
      type_no_gravity_planet_count += 1

print("Contador de planetas con tipo pero sin gravedad:", type_no_gravity_planet_count)
print("Planetas con gravedad y tipo de planeta", type_planet_count - type_no_gravity_planet_count)

goldilock_planet_count = 0
for key, value in final_dict.items():
   if "goldilock" in value:
      goldilock_planet_count += 1

print("Planetas encontrados con la característica \"Goldilock\":", goldilock_planet_count)

speed_planet_count = 0
for key, value in final_dict.items():
   if "speed" in value:
      speed_planet_count += 1

print("Planetas encontrados con la característica \"speed\":", speed_planet_count)


# Numeros flotantes, representación binaria
# 1111 1111 1111 1111
# signo decimales numero
# 0     0         10
# 0000 0000 0001 0010
# -10
# 1     0         10
# 1000 000 0001 0010
# -3.14
# 1     2         314
# 1010 0001 0011 1010


# Intento 1
final_dict = {}

for index, planet_data in enumerate(planet_data_rows):
   features_list = []
   gravity = (float(planet_data[3])*5.972e+24) / (float(planet_data[7])*float(planet_data[7])*6371000*6371000) * 6.674e-11

# Si la gravedad del planeta está dentro de lo aceptable, le agregamos la característica gravedad a la lista
   try:
      if gravity < 100:
         features_list.append("gravity")
   except : pass

# Si es el tipo terrestrial o super-tierra, le agregamos la característica tipo de planeta a la lista
   try :
      if planet_data[6].lower() == "terrestrial" or planet_data[6].lower() == "super earth" :
         features_list.append("planet_type")
   except: pass
# Si está dentro del rango Ricitos de Oro, le agregamos la característica goldilock a la lista
   try :
      # "1.29| |AU" --> ["1.29", "AU"]
      if float(planet_data[8].split(" ")[0]) > 0.38 and float(planet_data[8].split(" ")[0]) < 2 :
         features_list.append("goldilock")
   except: pass
# Si tiene una velocidad aceptable, le agregamos la caracterísitica speed a la lista
   try :
      distance = 2 * 3.14 * (float(planet_data[8].split(" ")[0]) *1.496e+8)
      time, unit = planet_data[9].split(" ")[0], planet_data[9].split(" ")[1]
      if unit.lower() == "days":
         time = float(time)
      else:
         time = float(time) * 365
      time = time * 86400
      speed = distance / time

      if speed < 200 :
         features_list.append("speed")
   except: pass
   final_dict[index] = features_list

# print("Diccionario final:", final_dict)


final_dict = {}

for index, planet_data in enumerate(planet_data_rows):
   features_list = []
   gravity = (float(planet_data[3])*5.972e+24) / (float(planet_data[7])*float(planet_data[7])*6371000*6371000) * 6.674e-11

# Si la gravedad del planeta está dentro de lo aceptable, le agregamos la característica gravedad a la lista
   try:
      if gravity < 100:
         features_list.append("gravity")
   except : pass

# Si es el tipo terrestrial o super-tierra, le agregamos la característica tipo de planeta a la lista
   try :
      if planet_data[6].lower() == "terrestrial" or planet_data[6].lower() == "super earth" :
         features_list.append("planet_type")
   except: pass
# Si está dentro del rango Ricitos de Oro, le agregamos la característica goldilock a la lista
      # "1.29| |AU" --> ["1.29", "AU"]
   try:
      if float(planet_data[8].split(" ")[0]) > 0.38 and float(planet_data[8].split(" ")[0]) < 2 :
         features_list.append("goldilock")    
   except:
      try:
         if planet_data[8] > 0.38 and planet_data[8] < 2 :
            features_list.append("goldilock")
      except: pass    
# Si tiene una velocidad aceptable, le agregamos la caracterísitica speed a la lista
   try :
      try:
         distance = 2 * 3.14 * (float(planet_data[8].split(" ")[0]) *1.496e+8)
      except:
        try:
          distance = 2 * 3.14 * (float(planet_data[8]) *1.496e+8)
        except: pass

      try:
        time, unit = planet_data[9].split(" ")[0], planet_data[9].split(" ")[1]
        if unit.lower() == "days":
          time = float(time)
        else:
          time = float(time) * 365
      except:
         time = planet_data[9]
      time = time * 86400
      speed = distance / time
      if speed < 200 :
        features_list.append("speed")
   except: pass
   final_dict[index] = features_list

# print("Diccionario final:", final_dict)

goldilock_planet_count = 0
for key, value in final_dict.items():
   if "goldilock" in value:
      goldilock_planet_count += 1

print("Planetas encontrados con la característica \"Goldilock\":", goldilock_planet_count)

speed_planet_count = 0
for key, value in final_dict.items():
   if "speed" in value:
      speed_planet_count += 1

print("Planetas encontrados con la característica \"speed\":", speed_planet_count)

goldilock_gravity_type_count = 0
for key, value in final_dict.items() :
   if "goldilock" in value and "planet_type" in value and "gravity" in value:
      goldilock_gravity_type_count += 1

print("Planetas con tipo, gravedad y que están en la zona Ricitos de Oro:", goldilock_gravity_type_count)

speed_goldilock_gravity_type_count = 0
for key, value in final_dict.items() :
   if "goldilock" in value and "planet_type" in value and "gravity" in value and "speed" in value:
      speed_goldilock_gravity_type_count += 1

print("Planetas con velocidad, tipo, gravedad y que están en la zona Ricitos de Oro:", speed_goldilock_gravity_type_count)

