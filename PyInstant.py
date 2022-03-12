from typing import Type
from redis import ConnectionPool, Redis

from Exceptions import MissingSSLCert

# PyInstant Will Implement The Singleton Design Pattern
# To Better Handle Connections To Redis

class PyInstant:

    __instance = None

    def __init__(self) -> None:
        
        if PyInstant.__instance != None:
            raise Exception("PyInstant is singleton")
        else:
            PyInstant.__instance = self

    @staticmethod
    def get_instance():

        if PyInstant.__instance is None:
            PyInstant()
        return PyInstant.__instance

    def create_connection(self, host: str, port: int, db: int = 0, ssl: bool = False, ssl_ca_certs: str = None) -> None:
        pass


