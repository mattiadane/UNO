from abc import ABC, abstractmethod


class Card(ABC):
    @property
    @abstractmethod
    def type(self):
        pass

    @property
    @abstractmethod
    def type_property(self):
        pass

    @type_property.setter
    @abstractmethod
    def type_property(self, val):
        ...

    @abstractmethod
    def __str__(self):
        pass
