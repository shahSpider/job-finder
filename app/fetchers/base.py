from abc import ABC, abstractmethod

class BaseFetcher(ABC):

    def __init__(self, source):
        self.source = source

    @abstractmethod
    async def fetch(self):
        pass

    @abstractmethod
    def parse(self, raw_data):
        pass