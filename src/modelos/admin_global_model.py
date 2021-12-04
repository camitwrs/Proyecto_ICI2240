import os
import random
import string
import shutil
import csv
from tempfile import NamedTemporaryFile
from src.cupon import Cupon


class AdminGlobalModel:
    """
        Clase que contiene la parte lógica del menú de un administrador global.
        Si desea, por ejemplo, implementar la opción de menú de mostrar_info_cine, se debería
        crear una función con nombre similar en esta clase que retorne los datos que la vista
        necesita desplegar.
    """
    def __init__(self, empleado, cines: dict, cupones: dict):
        self.empleado = empleado
        self.cines = cines
        self.cupones = cupones

    def generar_cupones(self, cantidad, porcentaje):
        new_cupones = {}

        for _ in range(cantidad):
            codigo = ''.join((random.choice(string.ascii_uppercase) for x in range(6)))

            if self.cupones.get(codigo) is None:
                new_cupon = Cupon(codigo, porcentaje, False)
                self.cupones[codigo] = new_cupon
                new_cupones[codigo] = new_cupon

        path = os.getcwd()
        abs_path_cupones = f"{path}\data\cupones.csv"
        
        with open(abs_path_cupones, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file, lineterminator='\n')
            for codigo, cupon in new_cupones.items():
                writer.writerow((codigo, cupon.descuento, "0"))

            csv_file.close()

        if len(new_cupones.items()) > 0:
            return True
        else:
            return False