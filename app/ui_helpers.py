# Este arquivo contém funções auxiliares para criar a interface do usuário
# São ferramentas reutilizadas em várias partes do sistema para criar elementos visuais

# Importa bibliotecas para criar interface gráfica
import customtkinter as ctk
from tkinter import ttk

def configurar_tema():
    """Configura o tema da aplicação."""
    # Define a aparência para o tema escuro (dark)
    ctk.set_appearance_mode("dark")
    # Define o esquema de cores para azul escuro
    ctk.set_default_color_theme("dark-blue")

def criar_entrada(pai, placeholder):
    """Cria um widget de entrada customizado."""
    # Cria e retorna uma caixa de texto com um texto de exemplo
    # O parâmetro 'pai' indica onde a caixa será colocada
    # 'placeholder_text' é o texto que aparece quando a caixa está vazia
    return ctk.CTkEntry(pai, placeholder_text=placeholder, width=300)

def criar_botao(pai, texto, comando):
    """Cria um botão customizado."""
    # Cria e retorna um botão com um texto e uma função
    # O parâmetro 'pai' indica onde o botão será colocado
    # 'text' é o texto que aparece no botão
    # 'command' é a função que será executada quando o botão for clicado
    return ctk.CTkButton(pai, text=texto, command=comando, width=200)

def criar_combobox(pai, valores=None):
    """Cria uma combobox."""
    # Cria uma caixa de seleção suspensa (dropdown)
    # O parâmetro 'pai' indica onde a combobox será colocada
    # 'values' são as opções disponíveis na lista
    combo = ttk.Combobox(pai, values=valores, width=30, state="readonly")
    # Se houver valores, seleciona o primeiro por padrão
    if valores:
        combo.current(0)
    return combo

def criar_tabela(pai, colunas, altura=10):
    """Cria uma tabela (Treeview)."""
    # Cria uma tabela com colunas especificadas
    # O parâmetro 'pai' indica onde a tabela será colocada
    # 'columns' são os nomes das colunas
    # 'show="headings"' mostra apenas os cabeçalhos (sem coluna de ícones)
    tabela = ttk.Treeview(pai, columns=colunas, show="headings", height=altura)
    
    # Configurando cabeçalhos
    for coluna in colunas:
        # Define o texto do cabeçalho
        tabela.heading(coluna, text=coluna)
        # Configura a largura e o alinhamento da coluna
        tabela.column(coluna, anchor="center", width=100)
    
    # Adiciona barra de rolagem vertical
    scrollbar = ttk.Scrollbar(pai, orient="vertical", command=tabela.yview)
    # Conecta a barra de rolagem à tabela
    tabela.configure(yscrollcommand=scrollbar.set)
    
    # Retorna a tabela e a barra de rolagem
    return tabela, scrollbar

def limpar_frame(frame):
    """Remove todos os widgets de um frame."""
    # Remove todos os elementos visuais de um container
    # Útil para limpar uma área antes de mostrar novos elementos
    for widget in frame.winfo_children():
        widget.destroy()

def mostrar_mensagem(titulo, mensagem, tipo="info"):
    """Exibe uma mensagem em uma janela modal."""
    # Importa a função de mensagem
    from tkinter import messagebox
    
    # Mostra diferentes tipos de mensagens com base no tipo solicitado
    if tipo == "info":
        # Mensagem informativa (ícone de informação)
        messagebox.showinfo(titulo, mensagem)
    elif tipo == "erro":
        # Mensagem de erro (ícone de erro)
        messagebox.showerror(titulo, mensagem)
    elif tipo == "aviso":
        # Mensagem de aviso (ícone de aviso)
        messagebox.showwarning(titulo, mensagem)
    else:
        # Se o tipo não for reconhecido, mostra como informação
        messagebox.showinfo(titulo, mensagem)

def validar_numero(valor):
    """Valida se um valor é numérico."""
    # Se o valor estiver vazio, retorna verdadeiro (permitindo campo vazio)
    if valor == "":
        return True
    try:
        # Tenta converter o valor para um número decimal
        float(valor)
        # Se conseguir, retorna verdadeiro (é um número válido)
        return True
    except ValueError:
        # Se não conseguir converter, retorna falso (não é um número)
        return False

def formatar_preco(valor):
    """Formata um valor para exibição como preço."""
    try:
        # Tenta converter o valor para número e formata como moeda
        # Por exemplo, 10.5 será formatado como "R$ 10.50"
        return f"R$ {float(valor):.2f}"
    except (ValueError, TypeError):
        # Se não conseguir converter, retorna zero formatado
        return "R$ 0,00"