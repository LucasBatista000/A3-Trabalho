import customtkinter as ctk
from PIL import Image
from telas.meuslivros import *
from telas.menuperfil import *


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Biblioteca Pessoal")
        self.geometry("1400x700")

        # Frame superior onde fica o frame dos botões
        self.frame_superior = ctk.CTkFrame(self, fg_color="#C3BCBC", height=75, corner_radius=0)
        self.frame_superior.pack(fill="x")
        
        # Frame para alocar os botões no meio do topo
        frame_botoes = ctk.CTkFrame(self.frame_superior, fg_color="transparent", corner_radius=0)
        frame_botoes.place(relx=0.5, rely=0.5, anchor="center")
        
        # Frame responsável pelo meio da tela ( Será trocado por outro frame ao apertar no botão )
        self.meio = ctk.CTkFrame(self, fg_color="white", corner_radius=0, border_width=0)
        self.meio.pack(side="top", fill="both", expand=True)

        self.meio.grid_rowconfigure(0, weight=1)
        self.meio.grid_columnconfigure(0, weight=1)
        
        # Chama a função que inicia o menu de botões
        self.configurar_menu_botoes()

        # Loop responsável por carregar os frames
        self.frames = {}
        for F in (MenuIniciar, MeusLivros, Perfil):
            frame = F(self.meio, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Inicia a função que mostra as telas
        self.mostrar_tela(MenuIniciar)

    def configurar_menu_botoes(self):
        frame_botoes = ctk.CTkFrame(self.frame_superior, fg_color="transparent", corner_radius=0)
        frame_botoes.place(relx=0.5, rely=0.5, anchor="center")
        
        icone_meus = ctk.CTkImage(light_image=Image.open("imagens/icone_meus_livros.png"), size=(30, 30))
        icone_relatorio = ctk.CTkImage(light_image=Image.open("imagens/icone_relatorio.png"), size=(30, 30))
        icone_sair = ctk.CTkImage(light_image=Image.open("imagens/icone_sair.png"), size=(30, 30))
        icone_perfil = ctk.CTkImage(light_image=Image.open("imagens/icone_perfil.png"), size=(30, 30))
        
        # Botões do menu inicial para entrada das funcionalidades e menus do sistema
        btn_menus = [
            ("Meus livros", lambda: self.mostrar_tela(MeusLivros), icone_meus),
            ("Relatórios", lambda: print("relatorios"), icone_relatorio),
            ("Meu perfil", lambda: self.mostrar_tela(Perfil), icone_perfil),
            ("Sair", lambda: self.destroy(), icone_sair)
        ]

        for nome, comando, icone in btn_menus:
            btn = ctk.CTkButton(frame_botoes, text=nome, text_color="black", height=50, width=50,
                compound="top", image=icone, fg_color="#C3BCBC", hover_color="#B0A8A8", 
                font=("Inter", 18),command=comando)
            btn.pack(side="left", padx=10, pady=10, anchor="center")

    def mostrar_tela(self, tela):
        frame = self.frames[tela]
        frame.tkraise()


class MenuIniciar(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, corner_radius=0)
        self.controller = controller
        self.configure(fg_color="transparent")

        titulo_central = ctk.CTkLabel(self, text="Biblioteca Pessoal", text_color="black", font=("Inter", 30, "bold"))
        titulo_central.place(relx=0.5, rely=0.5, anchor="center")

        print('RELATÓRIO: Tela inicial funcionando.')