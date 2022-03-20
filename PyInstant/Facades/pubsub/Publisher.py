from ...Exceptions import SingletonException
from ...Connection import Connection

class Publisher(Connection):

    __instance = None
    
    def __init__(self) -> None:
        
        self.pub_sub = super().get_instance().get_redis_connection().pubsub()

        if Publisher.__instance != None:
            raise SingletonException("This class Publisher is a Singleton")
        else:
            Publisher.__instance = self
    
    @staticmethod
    def get_instance():
        if Publisher.__instance is None:
            Publisher()
        return Publisher.__instance
    
    def emit(self, channel_name: str, data):
        super().get_instance().get_redis_connection().publish(channel_name, data)

    def get_data(self):
        return self.pub_sub.get_message()