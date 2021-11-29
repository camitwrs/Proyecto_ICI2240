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
            """ SE BORRA DEL CSV EMPLEADOS.CSV Y LA CARPETA DEL EMPLEADO """
            pass
            
        return result
