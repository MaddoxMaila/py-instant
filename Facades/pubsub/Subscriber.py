from Exceptions import SingletonException
from Connection import Connection

class Subscriber(Connection):
    
    __instance = None

    def __init__(self) -> None:
        
        self.pub_sub = super().get_instance().get_redis_connection().pubsub()

        if Subscriber.__instance is not None:
            raise SingletonException("This class Subscriber is a singleton")
        else:
            Subscriber.__instance = self
    
    @staticmethod
    def get_instance(self):
        if Subscriber.__instance is None:
            Subscriber()
        return Subscriber.__instance

    def add_channel(self, channel_name: str) -> None:
        self.pub_sub.subscribe(channel_name)

    def add_channels(self, channel_names: list) -> None:
        (self.add_channel(channel_name=channel_name) for channel_name in  channel_names)

    def channels_exists(self, channel_name: str or list) -> bool:
        pass