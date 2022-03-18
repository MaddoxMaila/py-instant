import imp
from ..Connection import Connection
from ..Facades import Subscriber
from ..Exceptions import ChannelTypeException
from redis.client import PubSub

class PubSub(Connection):
    
    def __init__(self) -> None:

        self.redis_connection = super().get_instance()

    def subscribe_channels(self, channel_name: str or list) -> None:
        
        if type(channel_name) is 'str':
            Subscriber.get_instance().add_channel(channel_name=channel_name)
        elif type(channel_name) is 'list':
            Subscriber.get_instance().add_channels(channel_names=channel_name)
        else:
            raise ChannelTypeException("Wrong type for a channel name")