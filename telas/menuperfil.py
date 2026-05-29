import customtkinter as ctk

TEXTO = "black"
BOTOES = "gray"
BOTOES_HOVER = "DarkGray"

class Perfil(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, corner_radius=0, fg_color="white")
        self.configure(fg_color="transparent")
        self.controller = controller
        
        topo = ctk.CTkFrame(self, fg_color="transparent", corner_radius=0)
        topo.pack(fill="x")
        meio = ctk.CTkFrame(self, fg_color="white", corner_radius=0)
        meio.pack(fill="both", expand=True)
        
        print("RELATÓRIO: Meus livros funcionando")