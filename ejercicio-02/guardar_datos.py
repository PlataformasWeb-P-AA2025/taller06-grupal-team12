from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import requests
from crear_entidad import Paises
import json

# Conexión a SQLite
engine = create_engine('sqlite:///basepaises.db')
Session = sessionmaker(bind=engine)
session = Session()

# Obtener JSON desde la web
archivo = requests.get("https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json")
datos_json = archivo.json()

# Iterar y guardar en la base
for d in datos_json:
    p = Paises(
        nombrePais=d.get('CLDR display name'),
        capital=d.get('Capital'),
        continente=d.get('Continent'),
        dial=d.get('Dial'),
        geonameId=int(d.get('Geoname ID')) if d.get('Geoname ID') else None,
        itu=d.get('ITU'),
        lenguaje=d.get('Languages'),
        independiente=d.get('is_independent')
    )
    session.add(p)

# Guardar cambios
session.commit()
