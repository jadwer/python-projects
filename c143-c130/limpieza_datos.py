import pandas as pd

planetas = pd.read_csv('planetas_datos.csv')
planetas = planetas.drop(['Unnamed: 0.1', 'Unnamed: 0', 'id'], axis=1)

print(planetas.shape)
print(planetas.head())

print(planetas.columns)

planetas = planetas.drop(['hyperlink', 'sy_snum', 'sy_pnum', 'disc_year', 'disc_facility', 'pl_controv_flag', 'pl_orbper', 'pl_orbpererr1', 'pl_orbpererr2', 'pl_orbperlim', 'pl_orbsmax', 'pl_orbsmaxerr1', 'pl_orbsmaxerr2', 'pl_orbsmaxlim', 'pl_rade', 'pl_radeerr1', 'pl_radeerr2', 'pl_radelim', 'pl_radj', 'pl_radjerr1', 'pl_radjerr2', 'pl_radjlim', 'pl_bmasse', 'pl_bmasseerr1', 'pl_bmasseerr2', 'pl_bmasselim', 'pl_bmassj', 'pl_bmassjerr1', 'pl_bmassjerr2', 'pl_bmassjlim', 'pl_bmassprov', 'pl_orbeccen', 'pl_orbeccenerr1', 'pl_orbeccenerr2', 'pl_orbeccenlim', 'pl_insolerr1', 'pl_insolerr2', 'pl_insollim', 'pl_eqt', 'pl_eqterr1', 'pl_eqterr2', 'pl_eqtlim', 'ttv_flag', 'st_spectype', 'st_tefferr1', 'st_tefferr2', 'st_tefflim', 'st_raderr1', 'st_raderr2', 'st_radlim', 'st_masserr1', 'st_masserr2', 'st_masslim', 'st_met', 'st_meterr1', 'st_meterr2', 'st_metlim', 'st_metratio', 'st_logg', 'st_loggerr1', 'st_loggerr2', 'st_logglim', 'ra', 'dec', 'sy_dist', 'sy_disterr1', 'sy_disterr2', 'sy_vmag', 'sy_vmagerr1', 'sy_vmagerr2', 'sy_kmag', 'sy_kmagerr1', 'sy_kmagerr2', 'sy_gaiamag', 'sy_gaiamagerr1', 'sy_gaiamagerr2'],axis=1)

print(planetas.columns)

print(planetas.head())

planetas = planetas.rename({
                'hostname': "solar_system_name", 
                'discoverymethod': "planet_discovery_method", 
                'pl_insol': "planet_orbital_inclination", 
                'rastr': "right_ascension", 
                'decstr': "declination", 
                "st_teff": "host_temperature", 
                'st_mass': "host_mass", 
                'st_rad': "host_radius"
            }, axis='columns')

planetas.head(50)

print(planetas.columns)

planetas.to_csv('main.csv', index=False)