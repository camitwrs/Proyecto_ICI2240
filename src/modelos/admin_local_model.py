import os
import csv
import shutil
from tempfile import NamedTemporaryFile


class AdminLocalModel:
    """
        Clase que contiene la parte lógica del menú de un administrador local.
        Si desea, por ejemplo, implementar la opción de menú de mostrar_horario, se debería
        crear una función con nombre similar en esta clase que retorne los datos que la vista
        necesita desplegar.
    """
    def __init__(self, empleado, cine):
        self.empleado = empleado
        self.cine = cine

    def get_empleados(self):
        empleados_list = []
        empleados = self.cine.get_empleados()

        for empleado in empleados:
            datos_tupla = (empleado[0], empleado[1].nombre, empleado[1].sueldo)
            empleados_list.append(datos_tupla)    

        return empleados_list

    def eliminar_empleado(self, rut):
        result = self.cine.eliminar_empleado(rut)

        if result: 
            path = os.getcwd()

            abs_path_credenciales = f"{path}\data\credenciales.csv"
            tempfile = NamedTemporaryFile(mode='a', delete=False)
            fields = ['rut', 'contraseña', 'cargo', 'cine']

            with open(abs_path_credenciales, 'r+', newline='') as csvfile, tempfile:
                reader = csv.DictReader(csvfile, fieldnames=fields)
                writer = csv.DictWriter(tempfile, fieldnames=fields, lineterminator='\n')
                for row in reader:
                    print(row['rut'], rut)
                    if row['rut'] == rut:  
                        print(row['rut'], rut)
                        continue
                    writer.writerow(row)

            shutil.move(tempfile.name, abs_path_credenciales)
            
            abs_path_empleados = f"{path}\data\{self.empleado.cine}\\empleados.csv"
            tempfile = NamedTemporaryFile(mode='a', delete=False)
            fields = ['nombre', 'rut', 'sueldo', 'ventas']

            with open(abs_path_empleados, 'r+', newline='') as csvfile, tempfile:
                reader = csv.DictReader(csvfile, fieldnames=fields)
                writer = csv.DictWriter(tempfile, fieldnames=fields, lineterminator='\n')
                for row in reader:
                    if row['rut'] == rut:  
                        continue
                    writer.writerow(row)

            shutil.move(tempfile.name, abs_path_empleados)

            abs_path_empleado_folder = f"{path}\data\{self.empleado.cine}\\empleados\{rut}"
            shutil.rmtree(abs_path_empleado_folder)

        return result

    def añadir_empleado(self, rut: str, contraseña: str, nombre_completo: str, sueldo: str):
        if self.cine.existe_empleado(rut):
            return None

        path = os.getcwd()
        abs_path_empleados = f"{path}\data\{self.empleado.cine}\\empleados.csv"
        abs_path_empleado_folder = f"{path}\data\{self.empleado.cine}\\empleados\{rut}\\"
        abs_path_credenciales = f"{path}\data\\credenciales.csv"

        # Se agrega el empleado al archivo credenciales.csv
        with open(abs_path_credenciales, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file, lineterminator='\n')
            writer.writerow((rut, contraseña, "empleado", self.cine.nombre))

            csv_file.close()

        # Se agrega el empleado al archivo empleados.csv
        with open(abs_path_empleados, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file, lineterminator='\n')
            writer.writerow((nombre_completo, rut, sueldo, 0))

            csv_file.close()

        os.makedirs(abs_path_empleado_folder)

        # Se crea el archivo horarios.csv
        with open(f"{abs_path_empleado_folder}\horarios.csv", 'w', newline='') as csv_file:
            writer = csv.writer(csv_file, lineterminator='\n')
            writer.writerow(("inicio", "final"))

            csv_file.close()

        # Se crea el archivo asistencia.csv
        with open(f"{abs_path_empleado_folder}\\asistencia.csv", 'w', newline='') as csv_file:
            writer = csv.writer(csv_file, lineterminator='\n')
            writer.writerow(("horario_inicio", "asistencia"))

            csv_file.close()

        empleado = self.cine.añadir_empleado(rut, contraseña, nombre_completo, sueldo)
        return empleado

    def get_salas(self):
        return self.cine.get_salas()

    def habilitar_sala(self, id):
        self.cine.habilitar_sala(id)
        
        path = os.getcwd()
        abs_path_empleados = f"{path}\data\{self.empleado.cine}\\salas.csv"
        tempfile = NamedTemporaryFile(mode='a', delete=False)
        fields = ['id', 'capacidad', 'estado']

        with open(abs_path_empleados, 'r+', newline='') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=fields)
            writer = csv.DictWriter(tempfile, fieldnames=fields, lineterminator='\n')
            for row in reader:
                if row['id'] == str(id):  
                    row['estado'] = '1'
                writer.writerow(row)

        shutil.move(tempfile.name, abs_path_empleados)

        return self.get_salas()

    def deshabilitar_sala(self, id):
        self.cine.deshabilitar_sala(id)
        
        path = os.getcwd()
        abs_path_empleados = f"{path}\data\{self.empleado.cine}\\salas.csv"
        tempfile = NamedTemporaryFile(mode='a', delete=False)
        fields = ['id', 'capacidad', 'estado']

        with open(abs_path_empleados, 'r+', newline='') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=fields)
            writer = csv.DictWriter(tempfile, fieldnames=fields, lineterminator='\n')
            for row in reader:
                if row['id'] == str(id):  
                    row['estado'] = '0'
                writer.writerow(row)

        shutil.move(tempfile.name, abs_path_empleados)

        return self.get_salas()
