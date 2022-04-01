from ...Exceptions import SingletonException
from ...Connection import Connection


class Cacher(Connection):

    __instance = None

    def __init__(self) -> None:
        
        self.redis = super().get_instance().get_redis_connection()

        if Cacher.__instance != None:
            raise SingletonException("This class Cacher is a Singleton")
        else:
            Cacher.__instance = self
    
    @staticmethod
    def get_instance():
        if Cacher.__instance is None:
            Cacher()
        return Cacher.__instance


    def make(self, key: str) -> None:
        
        # check if key exists in all data type storage fields