from ..Exceptions import SingletonException

class Cache:
    
    __instance = None

    def __init__(self) -> None:
        
        if Cache.__instance != None:
            raise SingletonException("This class Cache is a Singleton")
        else:
            Cache.__instance = self
    
    @staticmethod
    def get_instance():
        if Cache.__instance is None:
            Cache()
        return Cache.__instance
        