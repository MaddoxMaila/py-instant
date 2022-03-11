from typing import Type
from redis import ConnectionPool

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

    def connect(self, ) -> None:
        pass
