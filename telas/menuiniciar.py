import customtkinter as ctk
from PIL import Image
from telas.meuslivros import *


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Menu Iniciar")
        self.geometry("1980x900")

        self.frame_superior = ctk.CTkFrame(
            self, fg_color="#C3BCBC", height=75, corner_radius=0)
        self.frame_superior.pack(fill="x")
        frame_botoes = ctk.CTkFrame(
            self.frame_superior, fg_color="transparent", corner_radius=0)
        frame_botoes.place(relx=0.5, rely=0.5, anchor="center")

        self.meio = ctk.CTkFrame(self, fg_color="white", corner_radius=0)
        self.meio.pack(fill="both", expand=True)

        self.configurar_menu_botoes()

        self.frames = {}
        for F in (MenuIniciar, MeusLivros):
            frame = F(self.meio, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.mostrar_tela(MenuIniciar)

    def configurar_menu_botoes(self):
        frame_botoes = ctk.CTkFrame(
            self.frame_superior, fg_color="transparent", corner_radius=0)
        frame_botoes.place(relx=0.5, rely=0.5, anchor="center")
        # Botões do menu inicial para entrada das funcionalidades e menus do sistema
        btn_menus = [
            ("📚\nListar livros", lambda: print("listar")),
            ("📁\nMeus livros", lambda: self.mostrar_tela(MeusLivros)),
            ("📒\nCadastro Livros", lambda: print("livros")),
            ("🙍\nCadastro Leitor", lambda: print("leitor")),
            ("📊\nRelatórios", lambda: print("relatorios")),
            ("⚙️\nSair", lambda: self.destroy())
        ]

        for nome, comando in btn_menus:  # Laço for que cria os botões do menu inicial, utilizando a biblioteca customtkinter para estilização
            btn = ctk.CTkButton(frame_botoes, text=nome, text_color="black", height=50, width=50,
                                fg_color="#C3BCBC", hover_color="#B0A8A8", font=("Inter", 18), command=comando)
            btn.pack(side="left", padx=10, pady=10, anchor="center")

    def mostrar_tela(self, tela):
        frame = self.frames[tela]
        frame.tkraise()


class MenuIniciar(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, corner_radius=0)
        self.controller = controller
        self.configure(fg_color="transparent")

        imagem_carregada = Image.open("imagens/fundo.png")
        minha_imagem = ctk.CTkImage(
            light_image=imagem_carregada, size=(1980, 850))

        ctk.CTkLabel(self, image=minha_imagem, text=" ",
                     font=ctk.CTkFont(size=20)).place(relx=0.5, rely=0.5, anchor="center")

        titulo_central = ctk.CTkLabel(self, text="GERENCIAMENTO DA FAZENDA\n v1.0", font=(
            "Segoe UI", 50, "bold"), text_color="black", fg_color="transparent")
        titulo_central.place(relx=0.5, rely=0.5, anchor="center")
        print('RELATÓRIO: Tela inicial funcionando.')
