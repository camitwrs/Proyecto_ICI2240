from tkinter import Tk, messagebox
from src.vistas.login import PageLogin


class Aplicacion(Tk):
    #Crea la ventana 
    def __init__(self, controller):
        Tk.__init__(self)

        self.controller = controller

        self.title("C4U")
        self.geometry("960x540")
        self.configure(bg="#1C1C1C")
        self.resizable(0,0)
        self._frame = None
        
        #Llama a la página de LOGIN
        self.switch_frame(PageLogin)

    #Cambia entre páginas (frames)
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    def throw_messagebox(self, title: str, message: str):
        messagebox.showinfo(title, message)

    def throw_question(self, title: str, message: str):
        return messagebox.askokcancel(title, message)