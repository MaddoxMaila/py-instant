from typing import Type
from redis import Redis, ConnectionPool, ConnectionError

from ..Exceptions import MissingSSLCertException, SingletonException, ConnectionException

class Connection:
    """
        This class will handle & implement all Redis Connection logic
    """

    __instance = None

    def __init__(self) -> None:

        self.redis_host: str = None
        self.redis_port: int = None
        self.redis_db: int   = None
        self.redis_ssl: bool = False
        self.redis_ssl_ca_certs: str = None
        
        self.redis_pool_connection: ConnectionPool = None
        self.redis_connection: Redis = None

        if Connection.__instance is not None:
            raise SingletonException("This class Connection is a singleton")
        else:
            Connection.__instance = self

    @staticmethod
    def get_instance():
        if Connection.__instance is None:
            Connection()
        return Connection.__instance

    def connect(self) -> None:
        
        self.validate_connection_details()
        
        try:
            self.redis_connection = Redis(connection_pool=self.redis_pool_connection)
            return Connection.get_instance()
            
        except ConnectionError as ce:
            print(ce)
        
    def load_connection_details(self, host: str,
                                    port: int,
                                    db: int = 0,
                                    ssl: bool = False,
                                    ssl_ca_certs: str = None):
        self.redis_host = host
        self.redis_port = port
        self.redis_db = db

        self.ssl = ssl
        self.ssl_ca_certs = ssl_ca_certs

        return Connection.get_instance()

    def validate_connection_details(self) -> None:

        if self.ssl is True:
            if self.ssl_ca_certs is None:
                raise MissingSSLCertException("Missing SSL certificate. Provide full path")
            else:
                self.connect_with_ssl()
        else:
            if (
                type(self.redis_host) is str and self.redis_host is not ""
                ) and (
                    type(self.redis_port) is int and self.redis_host is not 0 and self.redis_port is not ""
                    ):
                self.connect_without_ssl()
            else:
                raise ConnectionException("Connection Aborted... Check your Host or Port")

    def connect_with_ssl(self) -> None:
        
        try:
            self.redis_pool_connection = ConnectionPool(
                host=self.redis_host,
                port=self.redis_port,
                db=self.redis_db,
                ssl=self.redis_ssl,
                ssl_ca_certs=self.redis_ssl_ca_certs
            )
        except ConnectionError as e:
            print(e)
            
    def connect_without_ssl(self)-> None:
        try:
            self.redis_pool_connection = ConnectionPool(
                host=self.redis_host,
                port=self.redis_port,
                db=self.redis_db,
            )
        except ConnectionError as e:
            print(e)

    def get_redis_connection(self) -> Redis:
        return self.redis_connection
    def get_redis_pool_connection(self) -> ConnectionPool:
        return self.redis_pool_connection
                