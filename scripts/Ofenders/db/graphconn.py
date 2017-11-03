import sys
sys.path.append('./offender')
from offender.offender import Offender

from neo4j.v1 import GraphDatabase, basic_auth

class DB:

    def __init__(self, url, user, pwd):

        self.driver = GraphDatabase.driver(url, auth=basic_auth(user, pwd))

    def close(self):
        self.driver.close()

    def open(self):
        self.session = self.driver.session()

    def create_node(self, Offender ):
        self.session.run("CREATE (a:Person {name: {name}, title: {title}})",
              name =Offender.get_name(),title= Offender.get_gang())
