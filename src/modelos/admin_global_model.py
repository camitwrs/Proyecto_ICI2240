class AdminGlobalModel:
    """
        Clase que contiene la parte lógica del menú de un administrador global.
        Si desea, por ejemplo, implementar la opción de menú de mostrar_info_cine, se debería
        crear una función con nombre similar en esta clase que retorne los datos que la vista
        necesita desplegar.
    """
    def __init__(self, empleado, cines: dict):
        self.empleado = empleado
        self.cines = cines
