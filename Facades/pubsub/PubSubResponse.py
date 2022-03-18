import json

class PubSubResponse:

    def __init__(self, response: dict) -> None:
        
        self.data    = response["data"]
        self.type       = response["type"]
        self.channel    = response["channel"]
        self.pattern    = response["pattern"]
