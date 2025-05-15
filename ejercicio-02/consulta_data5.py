from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

# se importa la clase(s) del
# archivo genera_tablas
from crear_entidad import Paises

from configuracion import engine

Session = sessionmaker(bind=engine)
session = Session()

paises= session.query(Paises).filter(or_(Paises.nombrePais.like('%uador%'),Paises.capital.like('%ito%'))).all()

for p in paises:
    print(p.nombrePais, "-", p.capital)