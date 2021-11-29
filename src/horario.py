from datetime import datetime

class Horario:
    def __init__(self, inicio, final):
        self.inicio = inicio
        self.final = final
        

    def same_week(self):
        """
            Función que compara un horario con la fecha actual.
            Retorna true si están en la misma semana, false en caso contrario.
        """
        now = datetime.today()

        return self.inicio.isocalendar()[1] == now.isocalendar()[1] and self.inicio.year == now.year

    def is_horario_actual(self):
        """
            Función que verifica si la hora actual es una hora válida de ingreso (se encuentra entre el horario.inicio y horario.final).
            Retorna true si se cumple, false en caso contrario.
        """
        now = datetime.now()

        return now > self.inicio and now < self.final 
