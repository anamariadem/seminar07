'''
write a ClientRepository class:
    -it keeps a list of clients(private)
    - functions to add a new client (raise ex if client with same id already in repo)
    - function that returns all clients
'''
from domain import *
class ClientRepository:
    def __init__(self):
        self._data = []

    def store(self,client):
        pass

    def delete(self,clientId):
        pass

    def find(self,clientId):
        pass

    def getAll(self):
        #return self._data
        #maybe copy here fore safety
        #return self._data[:]
        #even safer
        return copy.deepcopy(self._data)