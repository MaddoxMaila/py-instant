

from ...Connection import Connection


class CacheSave:

    def __init__(self, connection: Connection) -> None:
        
        self.connection = connection.get_redis_connection()
    
    def save():
        pass