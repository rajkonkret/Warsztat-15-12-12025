from abc import ABCMeta, abstractmethod


class IPojazd(metaclass=ABCMeta):

    @abstractmethod
    def spalanie(self, odl, jedn):
        raise NotImplemented

    @abstractmethod
    def koszty_przejazdu(self, odl, jedn, cena):
        raise NotImplemented
