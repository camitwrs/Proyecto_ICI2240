class Cupon:
    def __init__(self, codigo, descuento, utilizado):
        self.codigo = codigo
        self.descuento = descuento
        self.utilizado = utilizado

    def verificar(self):
        """ 
            Verifica si el cupón ha sido utilizado con anterioridad.
            Retorna True en caso de que aún este vigente y False en caso que haya sido ocupado.
        """
        if self.utilizado == False:
            return True

        return False