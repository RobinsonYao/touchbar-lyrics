from abc import ABC
from abc import abstractmethod


class OutputBase(ABC):

    @abstractmethod
    def send(self, text):
        pass