from Facades import Subscriber, Publisher

class PubSub(Subscriber, Publisher):
    
    def __init__(self) -> None:
        super().__init__()