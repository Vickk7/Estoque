# Este arquivo controla a tela de movimentação de estoque
# Aqui estão as funções para registrar entradas e saídas de produtos

# Importa bibliotecas para criar a interface gráfica
import customtkinter as ctk
from tkinter import ttk, messagebox

# Importa funções auxiliares para criar elementos visuais
from app.ui_helpers import (
    criar_entrada,
    criar_botao,
    limpar_frame,
    criar_tabela
)

# Importa funções para gerenciar o estoque
from app.stock_manager import (
    obter_produto,
    atualizar_quantidade,
    obter_movimentos
)

def mostrar_movimentacao(frame_pai):
    """Exibe a tela de movimentação de estoque (entrada/saída)."""
    # Limpa qualquer conteúdo anterior da tela
    limpar_frame(frame_pai)
    
    # Adiciona o título da tela
    ctk.CTkLabel(
        frame_pai, 
        text="Movimentação de Estoque", 
        font=("Arial", 20, "bold")
    ).pack(pady=20)
    
    # Cria o quadro (frame) principal da tela
    frame_main = ctk.CTkFrame(frame_pai)
    frame_main.pack(pady=10, padx=20, fill="both", expand=True)
    
    # Cria um sistema de abas (tabs) para separar entrada e saída
    tabs = ttk.Notebook(frame_main)
    
    # Cria quadros para cada aba
    tab_entrada = ctk.CTkFrame(tabs)
    tab_saida = ctk.CTkFrame(tabs)
    
    # Adiciona as abas ao sistema de abas
    tabs.add(tab_entrada, text="Entrada de Produtos")
    tabs.add(tab_saida, text="Saída de Produtos")
    tabs.pack(fill="both", expand=True)
    
    # Função que cria um formulário de movimentação reutilizado para entrada e saída
    def criar_form_movimentacao(container, tipo):
        # Cria um quadro para o formulário
        frame_form = ctk.CTkFrame(container)
        frame_form.pack(pady=10, padx=20, fill="both", expand=True)
        
        # Cria os campos do formulário
        # Campo para o código do produto
        ctk.CTkLabel(frame_form, text="Código do Produto:").pack(pady=5)
        entry_codigo = criar_entrada(frame_form, "Digite o código")
        entry_codigo.pack(pady=5)
        
        # Área para mostrar o nome do produto pesquisado
        label_nome = ctk.CTkLabel(frame_form, text="")
        label_nome.pack(pady=5)
        
        # Campo para a quantidade a ser movimentada
        ctk.CTkLabel(frame_form, text="Quantidade:").pack(pady=5)
        entry_quantidade = criar_entrada(frame_form, "Digite a quantidade")
        entry_quantidade.pack(pady=5)
        
        # Função executada quando o botão Buscar Produto é clicado
        def buscar_produto():
            # Obtém o código digitado
            codigo = entry_codigo.get()
            if not codigo:
                messagebox.showerror("Erro", "Digite o código do produto.")
                return
            
            # Procura o produto no estoque
            produto = obter_produto(codigo)
            if produto:
                # Se encontrar, mostra o nome do produto
                label_nome.configure(text=f"Produto: {produto['nome']}")
            else:
                # Se não encontrar, mostra mensagem de erro
                label_nome.configure(text="Produto não encontrado")
                messagebox.showerror("Erro", "Produto não encontrado.")
        
        # Função executada quando o botão Confirmar é clicado
        def movimentar():
            # Obtém o código e quantidade digitados
            codigo = entry_codigo.get()
            quantidade = entry_quantidade.get()
            
            # Verifica se os campos foram preenchidos
            if not codigo or not quantidade:
                messagebox.showerror("Erro", "Preencha todos os campos obrigatórios.")
                return
            
            try:
                # Converte a quantidade para número inteiro
                quantidade = int(quantidade)
                # Verifica se a quantidade é positiva
                if quantidade <= 0:
                    messagebox.showerror("Erro", "A quantidade deve ser maior que zero.")
                    return
                    
            except ValueError:
                # Se ocorrer erro na conversão, mostra mensagem de erro
                messagebox.showerror("Erro", "Quantidade inválida.")
                return
            
            
            # Atualiza a quantidade do produto no estoque
            if atualizar_quantidade(codigo, quantidade, tipo):
                # Se der certo, mostra mensagem de sucesso
                messagebox.showinfo("Sucesso", "Movimentação registrada com sucesso!")
                # Limpa os campos do formulário
                entry_codigo.delete(0, "end")
                entry_quantidade.delete(0, "end")
                label_nome.configure(text="")
                # Atualiza a tabela de movimentações
                carregar_movimentacoes()
            else:
                # Se der erro (ex: estoque insuficiente), mostra mensagem de erro
                messagebox.showerror("Erro", "Erro ao registrar movimentação.")
        
        # Cria um quadro para os botões
        frame_botoes = ctk.CTkFrame(frame_form)
        frame_botoes.pack(pady=10)
        
        # Adiciona os botões de busca e confirmação
        criar_botao(frame_botoes, "Buscar Produto", buscar_produto).pack(side="left", padx=5)
        criar_botao(frame_botoes, "Confirmar", movimentar).pack(side="left", padx=5)
    
    # Cria os formulários para entrada e saída de produtos
    criar_form_movimentacao(tab_entrada, "entrada")
    criar_form_movimentacao(tab_saida, "saida")

    # Cria um quadro para o histórico de movimentações
    frame_historico = ctk.CTkFrame(frame_pai)
    frame_historico.pack(pady=10, padx=20, fill="both", expand=True)

    # Adiciona o título da seção de histórico
    ctk.CTkLabel(
        frame_historico,
        text="Histórico de Movimentações",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    # Cria uma tabela para mostrar o histórico de movimentações
    colunas = ("Código", "Produto", "Tipo", "Quantidade", "Data")
    tabela, scrollbar = criar_tabela(frame_historico, colunas)
    tabela.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Função para carregar os dados do histórico de movimentações na tabela
    def carregar_movimentacoes():
        # Limpa todos os itens da tabela
        for item in tabela.get_children():
            tabela.delete(item)

        # Obtém os movimentos do estoque
        movimentos = obter_movimentos()
        # Adiciona cada movimento à tabela
        for mov in movimentos:
            # Obtém o nome do produto a partir do código
            produto = obter_produto(mov["codigo"])
            nome_produto = produto["nome"] if produto else "Produto não encontrado"
            # Insere uma linha na tabela
            tabela.insert("", "end", values=(
                mov["codigo"],
                nome_produto,
                mov["tipo"],
                mov["quantidade"],
                mov["data"]
            ))

    # Carrega os dados iniciais na tabela
    carregar_movimentacoes()