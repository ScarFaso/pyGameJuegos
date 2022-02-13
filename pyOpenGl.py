from email.mime import base

1 + 1

carga = "nose"

mega = carga + "toga"


class Prueba2:
    def __init__(self, puntos, vida, armas):
            self.p = puntos
            self.v = vida
            self.a = armas
    def arma_elegida(self, num):
            self.a[num]

toga = Prueba2(7, 80, ["minigan","revolver","tramontina"])

print (toga.a[0])