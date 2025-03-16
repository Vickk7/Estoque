# Este arquivo controla a tela de cadastro de produtos
# Aqui estão as funções que mostram o formulário para adicionar novos produtos ao estoque

# Importa bibliotecas para criar a interface gráfica e mensagens
import customtkinter as ctk
from tkinter import messagebox
import tkinter as tk

# Importa funções auxiliares para criar elementos visuais e validações
from app.ui_helpers import (
    criar_entrada, 
    criar_botao, 
    limpar_frame,
    validar_numero
)

# Importa a função que adiciona produtos ao estoque
from app.stock_manager import adicionar_produto

def mostrar_cadastro_produto(frame_pai):
    """Exibe o formulário de cadastro de produto."""
    # Limpa qualquer conteúdo anterior da tela
    limpar_frame(frame_pai)
    
    # Adiciona o título da tela
    ctk.CTkLabel(
        frame_pai, 
        text="Cadastro de Produto", 
        font=("Arial", 20, "bold")
    ).pack(pady=20)
    
    # Cria um quadro (frame) para organizar o formulário
    frame_form = ctk.CTkFrame(frame_pai)
    frame_form.pack(pady=10, padx=20, fill="both", expand=True)
    
    # Cria os campos do formulário com suas etiquetas
    
    # Campo para o código do produto
    ctk.CTkLabel(frame_form, text="Código:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    entry_codigo = criar_entrada(frame_form, "Digite o código")
    entry_codigo.grid(row=0, column=1, padx=10, pady=10, sticky="w")
    
    # Campo para o nome do produto
    ctk.CTkLabel(frame_form, text="Nome:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    entry_nome = criar_entrada(frame_form, "Digite o nome")
    entry_nome.grid(row=1, column=1, padx=10, pady=10, sticky="w")
    
    # Campo para o preço do produto
    ctk.CTkLabel(frame_form, text="Preço:").grid(row=3, column=0, padx=10, pady=10, sticky="e")
    entry_preco = criar_entrada(frame_form, "Digite o preço")
    entry_preco.grid(row=3, column=1, padx=10, pady=10, sticky="w")
    # Configura validação para aceitar apenas números e ponto no campo de preço
    vali = (frame_form.register(validar_numero), '%P')
    entry_preco.configure(validate="key", validatecommand=vali)
    
    # Campo para a quantidade do produto
    ctk.CTkLabel(frame_form, text="Quantidade:").grid(row=4, column=0, padx=10, pady=10, sticky="e")
    entry_quantidade = criar_entrada(frame_form, "Digite a quantidade")
    entry_quantidade.grid(row=4, column=1, padx=10, pady=10, sticky="w")
    # Configura validação para aceitar apenas números inteiros no campo de quantidade
    vali_int = (frame_form.register(lambda P: P == "" or P.isdigit()), '%P')
    entry_quantidade.configure(validate="key", validatecommand=vali_int)
    
    # Campo para a categoria do produto
    ctk.CTkLabel(frame_form, text="Categoria:").grid(row=5, column=0, padx=10, pady=10, sticky="e")
    entry_categoria = criar_entrada(frame_form, "Digite a categoria")
    entry_categoria.grid(row=5, column=1, padx=10, pady=10, sticky="w")
    
    # Função que é executada quando o botão Salvar é clicado
    def salvar():
        # Obtém os valores digitados nos campos
        codigo = entry_codigo.get()
        nome = entry_nome.get()
        preco = entry_preco.get()
        quantidade = entry_quantidade.get()
        categoria = entry_categoria.get()
        
        # Verifica se todos os campos foram preenchidos
        if not codigo or not nome or not preco or not quantidade or not categoria:
            messagebox.showerror("Erro", "Preencha todos os campos obrigatórios.")
            return
        
        try:
            # Converte o preço e quantidade para números
            preco = float(preco)
            quantidade = int(quantidade)
            
            # Verifica se os valores são positivos
            if preco < 0 or quantidade < 0:
                messagebox.showerror("Erro", "Preço e quantidade devem ser valores positivos.")
                return
                
        except ValueError:
            # Se ocorrer erro na conversão, mostra mensagem de erro
            messagebox.showerror("Erro", "Formato de preço ou quantidade inválido.")
            return
        
        # Chama a função que adiciona o produto ao estoque
        resultado = adicionar_produto(codigo, nome, preco, quantidade, categoria)
        
        if resultado:
            # Se der certo, mostra mensagem de sucesso
            messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
            # Limpa os campos do formulário para um novo cadastro
            for entry in [entry_codigo, entry_nome,
                          entry_preco, entry_quantidade, entry_categoria]:
                entry.delete(0, tk.END)
        else:
            # Se der erro, mostra mensagem de erro
            messagebox.showerror("Erro", "Erro ao cadastrar produto.")
    
    # Cria um quadro (frame) para os botões
    frame_botoes = ctk.CTkFrame(frame_form)
    frame_botoes.grid(row=6, column=0, columnspan=2, pady=20)
    
    # Adiciona os botões de Salvar e Limpar
    criar_botao(frame_botoes, "Salvar", salvar).pack(side="left", padx=10)
    # O botão Limpar apenas apaga o conteúdo de todos os campos
    criar_botao(frame_botoes, "Limpar", lambda: [
        w.delete(0, tk.END) for w in [entry_codigo, entry_nome, entry_preco, entry_quantidade, entry_categoria]
    ]).pack(side="left", padx=10)