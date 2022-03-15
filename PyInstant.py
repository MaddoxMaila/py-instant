from typing import Type
from .Exceptions import SingletonException
from Connection import Connection

# PyInstant Will Implement The Singleton Design Pattern
# To Better Handle Connections To Redis

class PyInstant:

    __instance = None
    __connection = None

    def __init__(self) -> None:
        
        if PyInstant.__instance != None:
            raise SingletonException("This class PyInstant is a Singleton")
        else:
            PyInstant.__instance = self
            PyInstant.__connection = Connection.get_instance()

    @staticmethod
    def get_instance():

        if PyInstant.__instance is None:
            PyInstant()
        return PyInstant.__instance

    def create_connection(self, host: str, port: int, db: int = 0, ssl: bool = False, ssl_ca_certs: str = None) -> None:
        
        PyInstant.__connection.load_connection_details(
            host=host,
            port=port,
            db=db,
            ssl=ssl,
            ssl_ca_certs=ssl_ca_certs
        ).connect()

    def get_raw_connections(self) -> dict:
        return {
            "redis": PyInstant.__connection.get_redis_connection(),
            "pool": PyInstant.__connection.get_redis_pool_connection()
        }




