# Este arquivo controla a tela de login e cadastro de usuários no sistema
# Aqui estão as funções que mostram os formulários de login e cadastro e processam as informações

# Importa bibliotecas para criar a interface gráfica e mensagens na tela
import customtkinter as ctk
from tkinter import messagebox

# Importa funções de outros arquivos do sistema
# Estas funções permitem verificar login, cadastrar usuários e controlar quem está logado
from app.user_manager import autenticar_usuario, cadastrar_usuario, definir_usuario_atual

# Importa funções que ajudam a criar elementos visuais como botões e caixas de texto
from app.ui_helpers import configurar_tema, criar_entrada, criar_botao

# Importa a função que inicia a janela principal após o login bem-sucedido
from app.main_window import iniciar_janela_principal

# Variáveis que serão usadas em várias funções deste arquivo
# Essas variáveis armazenam a janela e os campos de entrada de texto
janela = None
entry_nome = None
entry_senha = None
entry_nome_cad = None
entry_senha_cad = None
entry_email_cad = None

def iniciar_janela():
    """Configura a janela principal do login."""
    global janela
    # Cria uma nova janela
    janela = ctk.CTk()
    janela.title("Sistema de Controle de Estoque")

    # Calcula o tamanho e posição da janela para centralizá-la na tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    largura_janela = 600
    altura_janela = 400
    pos_x = (largura_tela - largura_janela) // 2
    pos_y = (altura_tela - altura_janela) // 2
    janela.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")
    
    # Impede que o usuário possa redimensionar a janela
    janela.resizable(False, False)
    # Define o tema visual da aplicação
    configurar_tema()

def tela_login():
    """Cria a tela de login."""
    global entry_nome, entry_senha
    # Remove todos os elementos que possam existir na janela
    for widget in janela.winfo_children():
        widget.destroy()

    # Cria um quadro (frame) para organizar os elementos na tela
    frame = ctk.CTkFrame(janela)
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Adiciona um título à tela
    ctk.CTkLabel(frame, text="Login de Acesso", font=("Arial", 24, "bold")).pack(pady=20)

    # Cria campo para digitar o nome de usuário
    entry_nome = criar_entrada(frame, "Usuário")
    entry_nome.pack(pady=10)

    # Cria campo para digitar a senha (os caracteres aparecem como *)
    entry_senha = criar_entrada(frame, "Senha")
    entry_senha.configure(show="*")
    entry_senha.pack(pady=10)

    # Cria botões para entrar no sistema ou ir para tela de cadastro
    criar_botao(frame, "Entrar", autenticar).pack(pady=10)
    criar_botao(frame, "Cadastrar-se", tela_cadastro).pack(pady=5)

def autenticar():
    """Processa a autenticação do usuário."""
    # Obtém o texto digitado nos campos de nome e senha
    nome = entry_nome.get()
    senha = entry_senha.get()

    # Verifica se os campos não estão vazios
    if not nome or not senha:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        return

    # Verifica se o nome e senha estão corretos
    if autenticar_usuario(nome, senha):
        # Se estiver tudo certo, registra o usuário como logado
        definir_usuario_atual(nome)
        messagebox.showinfo("Login", "Login realizado com sucesso.")
        # Fecha a janela de login e abre a janela principal do sistema
        janela.destroy()
        iniciar_janela_principal()
    else:
        # Se os dados estiverem errados, mostra mensagem de erro
        messagebox.showerror("Erro de Login", "Login ou senha incorretos.")

def tela_cadastro():
    """Cria a tela de cadastro."""
    global entry_nome_cad, entry_senha_cad, entry_email_cad
    # Remove todos os elementos que possam existir na janela
    for widget in janela.winfo_children():
        widget.destroy()

    # Cria um quadro (frame) para organizar os elementos na tela
    frame = ctk.CTkFrame(janela)
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Adiciona um título à tela
    ctk.CTkLabel(frame, text="Cadastrar Novo Usuário", font=("Arial", 24, "bold")).pack(pady=20)

    # Cria campos para digitar as informações do novo usuário
    entry_nome_cad = criar_entrada(frame, "Escolha um login")
    entry_nome_cad.pack(pady=10)

    entry_senha_cad = criar_entrada(frame, "Crie uma senha")
    entry_senha_cad.configure(show="*")
    entry_senha_cad.pack(pady=10)

    entry_email_cad = criar_entrada(frame, "Seu e-mail")
    entry_email_cad.pack(pady=10)

    # Cria botões para cadastrar ou voltar à tela de login
    criar_botao(frame, "Cadastrar", cadastrar).pack(pady=10)
    criar_botao(frame, "Voltar", tela_login).pack(pady=5)

def cadastrar():
    """Processa o cadastro do usuário."""
    # Obtém o texto digitado nos campos de nome, senha e email
    nome = entry_nome_cad.get()
    senha = entry_senha_cad.get()
    email = entry_email_cad.get()

    # Verifica se os campos não estão vazios
    if not nome or not senha or not email:
        messagebox.showerror("Erro", "Preencha todos os campos.")
        return

    # Tenta cadastrar o novo usuário
    if cadastrar_usuario(nome, senha, email):
        # Se deu certo, mostra mensagem de sucesso e volta para tela de login
        messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
        tela_login()
    else:
        # Se o nome de usuário já existir, mostra mensagem de erro
        messagebox.showerror("Erro", "Nome de usuário já existe.")

def iniciar_login():
    """Inicia a tela de login."""
    # Configura e mostra a janela de login
    iniciar_janela()
    tela_login()
    # Inicia o loop principal que mantém a janela aberta e responde aos eventos
    janela.mainloop()