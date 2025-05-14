from sqlalchemy import create_engine

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///basepersonas.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String, Boolean

class Paises(Base):
    __tablename__ = 'laspersonas'
    
    id = Column(Integer, primary_key=True)
    nombrePais = Column(String)
    capital = Column(String)
    continente = Column(String)
    dial = Column(String)
    geonameId = Column(Integer)
    itu = Column(String)
    lenguaje = Column(String)
    independiente = Column(Boolean)


Base.metadata.create_all(engine)

