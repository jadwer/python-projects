import pandas as pd

planetas = pd.read_csv("list_of_planets.csv")
mas_datos = pd.read_csv("PSCompPars.csv")

print(planetas.head())
print(mas_datos.head())

planetas["name"] = planetas["name"].str.lower()
mas_datos["pl_name"] = mas_datos["pl_name"].str.lower()
print(mas_datos.head())

# Estos datos están en memoria. Si cierras el programa aqui, no se guarda en ningún archivo
# pero puedes usarlos para hacer cálculos

print(planetas.shape)
print(mas_datos.shape)

# Eliminamos las columnas que no necesitamos de planetas ['discovery_date', 'mass', 'detection_method']
planetas.drop(columns=["discovery_date", "mass"], inplace=True)
mas_datos = mas_datos.sort_values('pl_name')
mas_datos.update({'id': range(0, 0 + len(mas_datos))})

print(planetas.head())

planetas_mas_datos = pd.merge(planetas, mas_datos, on="id")

print(planetas_mas_datos.head)

print(planetas_mas_datos.shape)
print(planetas_mas_datos.columns)

planetas_mas_datos.to_csv("planetas_datos.csv")