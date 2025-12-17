from ipojazd import IPojazd


class Pojazd(IPojazd):

    def __init__(self, opis):
        self.opis = opis

    def spalanie(self, odl, jedn):
        return jedn * 100 / odl

    def koszty_przejazdu(self, odl, jedn, cena):
        return self.spalanie(odl, jedn) * (odl / 100) * cena
