# Este arquivo controla a janela principal do sistema após o login
# Aqui está a interface com os menus e as diferentes telas do sistema

# Importa bibliotecas para criar a interface gráfica
import customtkinter as ctk
from tkinter import messagebox, simpledialog
import tkinter as tk

# Importa funções auxiliares para criar elementos visuais
from app.ui_helpers import configurar_tema, criar_botao, limpar_frame

# Importa função para obter o nome do usuário que está logado
from app.user_manager import obter_usuario_atual

# Importa as funções que mostram as diferentes telas do sistema:
# - Cadastro de produtos
# - Movimentação de estoque (entrada e saída)
# - Relatórios e consultas
from app.view import (
    mostrar_cadastro_produto,
    mostrar_movimentacao,
    mostrar_relatorios
)

# Variáveis que serão usadas em várias funções deste arquivo
janela_principal = None
frame_conteudo = None

def iniciar_janela_principal():
    """Configura e exibe a janela principal do sistema."""
    global janela_principal, frame_conteudo
    
    # Cria uma nova janela
    janela_principal = ctk.CTk()
    janela_principal.title("Sistema de Controle de Estoque")
    
    # Calcula o tamanho e posição da janela para centralizá-la na tela
    largura_tela = janela_principal.winfo_screenwidth()
    altura_tela = janela_principal.winfo_screenheight()
    largura_janela = 1024
    altura_janela = 768
    pos_x = (largura_tela - largura_janela) // 2
    pos_y = (altura_tela - altura_janela) // 2
    janela_principal.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")
    
    # Define o tema visual da aplicação
    configurar_tema()
    # Configura o layout da janela (menu lateral e área de conteúdo)
    configurar_layout()
    # Inicia o loop principal que mantém a janela aberta e responde aos eventos
    janela_principal.mainloop()

def configurar_layout():
    """Configura o layout da janela principal."""
    global frame_conteudo
    
    # Cria o menu lateral (barra de navegação)
    frame_menu = ctk.CTkFrame(janela_principal, width=200)
    frame_menu.pack(side="left", fill="y", padx=10, pady=10)
    
    # Mostra o nome do usuário logado no topo do menu
    usuario_atual = obter_usuario_atual()
    ctk.CTkLabel(
        frame_menu, 
        text=f"Olá, {usuario_atual}", 
        font=("Arial", 16, "bold")
    ).pack(pady=(20, 30))
    
    # Adiciona os botões do menu para navegar entre as telas
    criar_botao(frame_menu, "Cadastrar Produto", lambda: navegar_para("cadastro")).pack(pady=10)
    criar_botao(frame_menu, "Movimentar Estoque", lambda: navegar_para("movimentacao")).pack(pady=10)
    criar_botao(frame_menu, "Relatórios", lambda: navegar_para("relatorios")).pack(pady=10)
    criar_botao(frame_menu, "Sair", sair).pack(pady=(50, 10))
    
    # Cria a área principal onde o conteúdo das telas será mostrado
    frame_conteudo = ctk.CTkFrame(janela_principal)
    frame_conteudo.pack(side="right", fill="both", expand=True, padx=10, pady=10)
    
    # Mostra a tela inicial com instruções
    mostrar_pagina_inicial()

def mostrar_pagina_inicial():
    """Exibe a página inicial do sistema."""
    # Limpa qualquer conteúdo que possa estar na área principal
    limpar_frame(frame_conteudo)
    
    # Cria um container centralizado para mostrar as informações
    frame_centro = ctk.CTkFrame(frame_conteudo)
    frame_centro.pack(expand=True)
    
    # Adiciona o título do sistema
    ctk.CTkLabel(
        frame_centro, 
        text="Sistema de Controle de Estoque", 
        font=("Arial", 28, "bold")
    ).pack(pady=20)
    
    # Adiciona instruções para o usuário
    ctk.CTkLabel(
        frame_centro, 
        text="Selecione uma opção no menu lateral",
        font=("Arial", 16)
    ).pack(pady=10)
    
    # Mostra a data e hora atual
    from datetime import datetime
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    ctk.CTkLabel(
        frame_centro, 
        text=f"Data: {data_hora}",
        font=("Arial", 14)
    ).pack(pady=30)

def navegar_para(destino):
    """Navega para uma seção específica do sistema."""
    # Direciona para a tela selecionada no menu
    if destino == "cadastro":
        # Mostra a tela de cadastro de produtos
        mostrar_cadastro_produto(frame_conteudo)
    elif destino == "movimentacao":
        # Mostra a tela de movimentação de estoque (entrada/saída)
        mostrar_movimentacao(frame_conteudo)
    elif destino == "relatorios":
        # Mostra a tela de relatórios e consultas
        mostrar_relatorios(frame_conteudo)
    else:
        # Se o destino não for reconhecido, volta para a página inicial
        mostrar_pagina_inicial()

def sair():
    """Encerra o programa."""
    # Pede confirmação antes de fechar o sistema
    if messagebox.askyesno("Sair", "Deseja realmente sair do sistema?"):
        # Fecha a janela principal
        janela_principal.destroy()