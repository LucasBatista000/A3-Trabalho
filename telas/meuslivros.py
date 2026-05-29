import customtkinter as ctk


class MeusLivros(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, corner_radius=0, fg_color="white")
        self.configure(fg_color="transparent")
        self.controller = controller
        
        meio = ctk.CTkFrame(self, fg_color="white", corner_radius=0)
        meio.pack(fill="both", expand=True)
        
        print("Meus livros funcionando")