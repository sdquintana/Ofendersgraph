from  offender.offender import Offender
from  db.graphconn import DB

if __name__ == '__main__':
     #Instanciamos la Clase
     of=Offender()
     of.set_name('malo')
     of.set_gang('banda')
     db= DB('bolt://localhost:7687', 'neo4j','holamundo')


     print(of.get_name())

     db.open()
     db.create_node(of)
     db.close()