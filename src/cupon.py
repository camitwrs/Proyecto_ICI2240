class Cupon:
    def __init__(self, codigo, descuento, utilizado):
        self.codigo = codigo
        self.descuento = descuento
        self.utilizado = utilizado

    def verificar(self):
        if self.utilizado == False:
            return True

        return False