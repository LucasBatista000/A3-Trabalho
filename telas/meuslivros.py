import customtkinter as ctk
from tkinter import ttk

TEXTO = "black"
BOTOES = "gray"
BOTOES_HOVER = "DarkGray"
LINHA_PAR = "#F8FAFC"
LINHA_IMPAR = "#EEF2F7"

class MeusLivros(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, corner_radius=0, fg_color="white")
        self.configure(fg_color="transparent")
        self.controller = controller
        
        topo = ctk.CTkFrame(self, fg_color="transparent", corner_radius=0)
        topo.pack(fill="x")
        meio = ctk.CTkFrame(self, fg_color="white", corner_radius=0)
        meio.pack(fill="both", expand=True)
        
        ctk.CTkLabel(topo, text="Pesquisar", font=("Inter", 12, "bold"), text_color=TEXTO).place(x=20, y=-5)
        
        self.entry_pesquisa = ctk.CTkEntry(topo, font=("Inter", 14), text_color="white", width=250)
        self.entry_pesquisa.pack(side="left", padx=15, pady=20)
        
        btn = [
            ("Pesquisar", lambda: print("pesquisa")),
            ("Cadastrar Livro", lambda: print("cadastrar livro"))
        ]
        
        for nome, comando in btn:
            ctk.CTkButton(topo, text=nome, text_color=TEXTO, fg_color=BOTOES, 
                            hover_color=BOTOES_HOVER, command=comando).pack(side="left", padx=10)
            
        
        # Tabela
        
        colunas = ("id", "nome", "qntpag", "status", "dataadicao")
        self.tabela = ttk.Treeview(meio, columns=colunas, show="headings")

        self.tabela.tag_configure("par", background=LINHA_PAR)
        self.tabela.tag_configure("impar", background=LINHA_IMPAR)
        
        self.tabela.heading("id", text="ID")
        self.tabela.heading("nome", text="Nome do Livro")
        self.tabela.heading("qntpag", text="Quant. de pág")
        self.tabela.heading("status", text="Status")
        self.tabela.heading("dataadicao", text="Data de adição")
        
        self.tabela.column("id", anchor="center")
        self.tabela.column("nome", anchor="center")
        self.tabela.column("qntpag", anchor="center")
        self.tabela.column("status", anchor="center")
        self.tabela.column("dataadicao", anchor="center")
        
        self.tabela.pack(fill="both", expand=True, padx=20, pady=20)
        
        print("RELATÓRIO: Menu MeusLivros funcionando")